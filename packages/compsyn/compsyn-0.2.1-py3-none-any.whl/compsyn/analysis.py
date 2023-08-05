# analysis code

import numpy as np
import scipy.stats
import time
import matplotlib.colors as mplcolors
import compsyn as cs
from numba import jit
import os
import PIL


def kl_divergence(dist1, dist2, symmetrized=True):
    if symmetrized==True:
        return (scipy.stats.entropy(dist1,dist2)+scipy.stats.entropy(dist2,dist1))/2.
    else:
        return scipy.stats.entropy(dist1,dist2)

def js_divergence(dist1, dist2):
    mean_dist = (dist1 + dist2)/2.
    return (scipy.stats.entropy(dist1, mean_dist) + scipy.stats.entropy(dist2, mean_dist))/2.


class ImageAnalysis():
    def __init__(self, image_data):
        #assert isinstance(image_data, compsyn.ImageData)
        self.image_data = image_data
        self.jzazbz_dict = image_data.jzazbz_dict
        self.rgb_dict = image_data.rgb_dict
        self.labels_list = image_data.labels_list
        # vals for vis
        self.rgb_vals_dict = image_data.rgb_vals_dict
        self.rgb_vals_dist_dict = image_data.rgb_vals_dist_dict
    # @jit
    def compute_color_distributions(self, labels, color_rep=['jzazbz', 'hsv', 'rgb'], spacing=36, num_bins=8, num_channels=3):
        dims = self.image_data.dims
        labels = labels if isinstance(labels, list) else [labels]
        self.jzazbz_dist_dict, self.hsv_dist_dict = {}, {}
        self.rgb_ratio_dict, self.rgb_dist_dict = {}, {}
        color_rep = [i.lower() for i in color_rep]
        
        if 'jzazbz' in color_rep:
            self.jzazbz_dist_dict = {}
            for key in labels:
                if key not in self.image_data.labels_list:
                    print("\nlabel {} does not exist".format(key))
                    continue
                if key not in self.image_data.jzazbz_dict.keys():
                    self.image_data.store_jzazbz_from_rgb(key)
                jzazbz, dist_array = [], []
                imageset = self.jzazbz_dict[key]
                for i in range(len(imageset)):
                    jzazbz.append(imageset[i])
                    dist = np.ravel(np.histogramdd(np.reshape(imageset[i][:,:,:],(dims[0]*dims[1],num_channels)),
                                          bins=(np.linspace(0,0.167,1+int(num_bins**(1./num_channels))),np.linspace(-0.1,0.11,1+int(num_bins**(1./num_channels))),
                                               np.linspace(-0.156,0.115,1+int(num_bins**(1./num_channels)))), density=True)[0])
                    dist_array.append(dist)
                self.jzazbz_dist_dict[key] = dist_array
        if 'hsv' in color_rep:
            self.h_dict, self.s_dict, self.v_dict = {}, {}, {}
            self.hsv_dist_dict = {}
            for key in labels:
                if key not in self.image_data.labels_list:
                    print("\nlabel {} does not exist".format(key))
                    continue
                imageset = self.rgb_dict[key]
                dist_array, h, s, v = [], [], [], []
                for i in range(len(imageset)):
                    hsv_array = mplcolors.rgb_to_hsv(imageset[i]/255.)
                    dist = np.histogram(360.*np.ravel(hsv_array[:,:,0]),
                                        bins=np.arange(0,360+spacing,spacing),
                                        density=True)[0]
                    dist_array.append(dist)
                    h.append(np.mean(np.ravel(hsv_array[:,:,0])))
                    s.append(np.mean(np.ravel(hsv_array[:,:,1])))
                    v.append(np.mean(np.ravel(hsv_array[:,:,2])))
                self.hsv_dist_dict[key] = dist_array
                self.h_dict[key], self.s_dict[key], self.v_dict[key] = h, s, v
        if 'rgb' in color_rep:
            self.rgb_ratio_dict, self.rgb_dist_dict = {}, {}
            for key in labels:
                if key not in self.image_data.labels_list:
                    print("\nlabel {} does not exist".format(key))
                    continue
                imageset = self.rgb_dict[key]
                rgb = []
                dist_array = []
                for i in range(len(imageset)):
                    r = np.sum(np.ravel(imageset[i][:,:,0]))
                    g = np.sum(np.ravel(imageset[i][:,:,1]))
                    b = np.sum(np.ravel(imageset[i][:,:,2]))
                    tot = 1.*r+g+b
                    rgb.append([r/tot,g/tot,b/tot])
                    dist = np.ravel(np.histogramdd(np.reshape(imageset[i],(dims[0]*dims[1],num_channels)),
                                          bins=(np.linspace(0,255,1+int(num_bins**(1./num_channels))),np.linspace(0,255,1+int(num_bins**(1./num_channels))),
                                               np.linspace(0,255,1+int(num_bins**(1./num_channels)))), density=True)[0])
                    dist_array.append(dist)
                self.rgb_ratio_dict[key] = rgb
                self.rgb_dist_dict[key] = dist_array
    # @jit
    def cross_entropy_between_images(self, symmetrized=True):
        #needswork
        rgb_dict = self.image_data.rgb_dict
        entropy_dict = {}
        entropy_dict_js = {}
        for key in rgb_dict:
            entropy_array = []
            entropy_array_js = []
            for i in range(len(rgb_dict[key])):
                for j in range(len(rgb_dict[key])):
                    if symmetrized == True:
                        mean = (rgb_dict[key][i] + rgb_dict[key][j])/2.
                        entropy_array.append((scipy.stats.entropy(rgb_dict[key][i],rgb_dict[key][j])+scipy.stats.entropy(rgb_dict[key][j],rgb_dict[key][i]))/2.)
                        entropy_array_js.append((scipy.stats.entropy(rgb_dict[key][i],mean) + scipy.stats.entropy(rgb_dict[key][j],mean))/2.)
                    else:
                        entropy_array.append(scipy.stats.entropy(rgb_dict[key][i],rgb_dict[key][j]))
            entropy_dict[key] = entropy_array
            entropy_dict_js[key] = entropy_array_js
        
        self.entropy_dict = entropy_dict
        self.entropy_dict_js = entropy_dict_js
        return entropy_dict, entropy_dict_js

    # @jit
    def cross_entropy_between_labels(self, symmetrized=True):
        color_dict = self.jzazbz_dist_dict
        words = self.labels_list
        mean_color_dict = {}
        
        for key in color_dict:
            mean_color_array = np.mean(np.array(color_dict[key]),axis=0)
            mean_color_dict[key] = mean_color_array
        labels_entropy_dict = {}
        labels_entropy_dict_js = {}
        color_sym_matrix = []
        color_sym_matrix_js = []
        
        for word1 in words:
            row = []
            row_js = []
            for word2 in words:
                if symmetrized == True:
                    mean = (mean_color_dict[word1] + mean_color_dict[word2])/2.
                    entropy = kl_divergence(mean_color_dict[word1],mean_color_dict[word2], symmetrized)
                    entropy_js = js_divergence(mean_color_dict[word1], mean_color_dict[word2])
                else:
                    entropy = scipy.stats.entropy(mean_color_dict[word1], mean_color_dict[word2])
                    entropy_js = []
                row.append(entropy)
                row_js.append(entropy_js)
                #these lines are for convenience; if strings are correctly synced across all data they are not needed
                if word1 == 'computer science':
                    labels_entropy_dict['computer_science' + '_' + word2] = entropy
                    labels_entropy_dict_js['computer_science' + '_' + word2] = entropy_js
                elif word2 == 'computer science':
                    labels_entropy_dict[word1 + '_' + 'computer_science'] = entropy
                    labels_entropy_dict_js[word1 + '_' + 'computer_science'] = entropy_js
                else:
                    labels_entropy_dict[word1 + '_' + word2] = entropy
                    labels_entropy_dict_js[word1 + '_' + word2] = entropy_js
            color_sym_matrix.append(row)
            color_sym_matrix_js.append(row_js)

        self.cross_entropy_between_labels_dict = labels_entropy_dict
        self.cross_entropy_matrix = color_sym_matrix
        self.cross_entropy_between_labels_dict_js = labels_entropy_dict_js
        self.cross_entropy_matrix_js = color_sym_matrix_js

    # @jit
    def cross_entropy_between_all_images(color_dict, words):
        entropy_dict_all = {}
        color_sym_matrix_js = []
        for word1 in words:
            row_js = []
            for word2 in words:
                entropy_js = []
                for i in range(len(color_dict[word1])):
                    for j in range(len(color_dict[word2])):
                        try:
                            mean = (color_dict[word1][i] + color_dict[word2][j])/2.
                            entropy_js.append(scipy.stats.entropy(color_dict[word1][i],mean) + scipy.stats.entropy(color_dict[word2][j],mean))/2.
                        except:
                            entropy_js.append(np.mean(entropy_js))
                entropy_dict_all[word1 + '_' + word2] = entropy_js
                row_js.append(np.mean(entropy_js))
            color_sym_matrix_js.append(row_js)
        return entropy_dict_all, color_sym_matrix_js

    # @jit
    def compress_color_data(self):
        avg_rgb_dict = {} #dictionary of average color coordinates
        for label in self.labels_list:
            try:
                avg_rgb = np.mean(np.mean(np.mean(self.jzazbz_dict[label],axis=0),axis=0),axis=0)
                avg_rgb_dict[label] = avg_rgb
            except:
                print(label + " failed")
                pass
        self.avg_rgb_dict = avg_rgb_dict

        jzazbz_dict_simp = {}
        for label in self.labels_list:
            avg_jzazbz = np.mean(self.jzazbz_dist_dict[label], axis=0)
            jzazbz_dict_simp[label] = avg_jzazbz
        self.jzazbz_dict_simp = jzazbz_dict_simp 

    # @jit
    # def compress_img_array(self, img_array_dict, words, compress_dim=300):
    #     compressed_img_array_dict = {}
    #     for word in words:
    #         print("Creating image array for " + word)
    #         compressed_img_array = np.zeros((compress_dim, compress_dim,3))
    #         for n in range(len(img_array_dict[word])):
    #             if np.shape(img_array_dict[word][n]) == (compress_dim, compress_dim, 3):
    #                 for i in range(compress_dim):
    #                     for j in range(compress_dim):
    #                         compressed_img_array[i][j] += img_array_dict[word][n][i][j]/(1.*len(img_array_dict[word]))
    #         compressed_img_array_dict[word] = compressed_img_array
    #     return compressed_img_array_dict


    def get_composite_image(self, labels=None, compress_dim=300, num_channels=3):
        compressed_img_dict = {}
        img_data = self.image_data.rgb_dict
        if not labels:
            labels = img_data.keys()
        for label in labels:
            print(label + " is being compressed.")
            compressed_img_dict[label] = np.zeros((compress_dim,compress_dim,num_channels))
            compressed_img_dict[label] = np.sum(img_data[label],axis=0)/(1.*len(img_data[label]))
            
        self.compressed_img_dict = compressed_img_dict
        return compressed_img_dict


    def save_colorgram_to_disk(self):
        if not os.path.exists('colorgrams'):
            os.makedirs('colorgrams')

        if len(self.compressed_img_dict) > 0:
            for img in self.compressed_img_dict:
                colorgram = PIL.Image.fromarray(self.compressed_img_dict[img].astype(np.uint8))
                colorgram.save(os.path.join("colorgrams", img + "_colorgram.png"))