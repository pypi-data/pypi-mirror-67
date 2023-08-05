
import matplotlib.colors as colors
import matplotlib.cm as cm
import colorsys
import seaborn as sns
import PIL
from PIL import Image

import colorsys
import matplotlib.colors as colors
from numba import jit

from sklearn.cluster import KMeans
import pickle
import scipy
import pylab
import scipy.cluster.hierarchy as sch
from scipy.spatial.distance import squareform
from scipy.spatial import ConvexHull
from scipy.ndimage import gaussian_filter
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.ticker import MaxNLocator
import matplotlib.pyplot as plt
import os
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
import numpy as np

from sklearn.manifold import TSNE
import gzip


cmap = cm.plasma(np.linspace(0.0, 0.5, 3))
sch.set_link_color_palette([colors.rgb2hex(rgb[:3]) for rgb in cmap])

def getImage(path):
    return OffsetImage(plt.imread(path), zoom=0.2)

class Visualisation():

    def __init__(self, image_analysis):
    #assert isinstance(image_data, compsyn.ImageData)
        self.image_analysis = image_analysis
        self.compressed_img_dict = self.image_analysis.compressed_img_dict
        self.jzazbz_dict = self.image_analysis.jzazbz_dict
        self.labels_list = self.image_analysis.labels_list
        self.rgb_dict = self.image_analysis.rgb_dict

    def jzazbz_color_distribution(self, label, num_channels=3):

        ind = np.random.rand(90000)
        rgblist = self.compressed_img_dict[label].reshape(90000,num_channels)

        x = np.mean(np.array(self.jzazbz_dict[label]),axis=0).reshape(90000,num_channels)[:,1]
        x_smooth = x#gaussian_filter(x, sigma=2.5)
        x_smooth = x_smooth[ind>0.75]

        y = np.mean(np.array(self.jzazbz_dict[label]),axis=0).reshape(90000,num_channels)[:,2]
        #y = y[ind>0.95]
        y_smooth = y#gaussian_filter(y, sigma=2.5)
        y_smooth = y_smooth[ind>0.75]

        z = np.mean(np.array(self.jzazbz_dict[label]),axis=0).reshape(90000,num_channels)[:,0]
        #z = z[ind>0.95]
        z_smooth = z#gaussian_filter(z, sigma=2.5)
        z_smooth = z_smooth[ind>0.75]

        fig = plt.figure(figsize=(8,6))
        ax = fig.add_subplot(111, projection='3d')

        ax.scatter(x_smooth, y_smooth, z_smooth/0.167, c=(1.25*rgblist[ind>0.75]/255.).clip(max=1.0), alpha=0.05, s=3.5)#, alpha=0.005)
        ax.xaxis.set_major_locator(MaxNLocator(5))
        ax.yaxis.set_major_locator(MaxNLocator(5))
        ax.zaxis.set_major_locator(MaxNLocator(5))

        ax.set_xlabel(r'$A_z$', fontsize=20, labelpad=12)
        ax.set_ylabel(r'$B_z$', fontsize=20, labelpad=12)
        ax.set_zlabel(r'$J_z$', fontsize=20, labelpad=8)
        ax.set_title(label, fontsize=22, 
                     color=np.mean(rgblist[ind>0.75]/255, axis=0), y=1.045)

        if not os.path.isdir('Figures/'): os.mkdir('Figures/')
        plt.savefig('Figures/' + label + '_full_dist.png')
        plt.show()


    def plot_labels_in_space(self, n_clusters=2):

        self.rgb_vals_dict = self.image_analysis.rgb_vals_dict
        self.rgb_vals_dist_dict = self.image_analysis.rgb_vals_dist_dict

        self.jzazbz_dist_dict = self.image_analysis.jzazbz_dist_dict
        self.avg_rgb_dict = self.image_analysis.avg_rgb_dict

        avg_dist_dict = {}
        for label in self.labels_list:
            avg_dist = np.mean(self.jzazbz_dist_dict[label],axis=0)
            avg_dist_dict[label] = avg_dist
            
        X = np.zeros((len(self.labels_list),8))
        i = 0
        for label in self.labels_list:
            X[i] = avg_dist_dict[label]
            i +=1
            
        kmeans = KMeans(n_clusters=n_clusters)#manually set number of clusters from clustering analysis 
        kmeans.fit(X)

        labels = kmeans.predict(X)
        centroids = kmeans.cluster_centers_

        colorsmap = map(lambda x: {1: 'r', 0: 'b', 2: 'g', 3:'m', 4:'k', 5:'brown'}, labels)

        fig = plt.figure(figsize=(8,6))
        ax = fig.add_subplot(111, projection='3d')
            
        ax.set_xlabel(r'$A_z$', fontsize=20, labelpad=10)
        ax.set_ylabel(r'$B_z$', fontsize=20, labelpad=10)
        ax.set_zlabel(r'$J_z$', fontsize=20, labelpad=10)

        for word in np.array(self.labels_list)[labels==0]:
            ax.scatter(self.avg_rgb_dict[word][1], self.avg_rgb_dict[word][2], self.avg_rgb_dict[word][0], 
                       c=1.65*np.mean(self.rgb_vals_dict[word],axis=0), label=word, s=30, marker='^')

        for word in np.array(self.labels_list)[labels==1]:
            ax.scatter(self.avg_rgb_dict[word][1], self.avg_rgb_dict[word][2], self.avg_rgb_dict[word][0], 
                       c=1.65*np.mean(self.rgb_vals_dict[word],axis=0), label=word, s=30, marker='o')

        for word in np.array(self.labels_list)[labels==2]:
            ax.scatter(self.avg_rgb_dict[word][1], self.avg_rgb_dict[word][2], self.avg_rgb_dict[word][0], 
                       c=1.65*np.mean(self.rgb_vals_dict[word],axis=0), label=word, s=30, marker='x')

        semantic_domain = 'Test_Words'
        ax.set_title(semantic_domain, fontsize=22, y=1.045)#, color=np.mean(rgblist[ind>0.75]/255, axis=0), y=1.045)
        ax.set_zlim(0.05,0.12)
        ax.set_xlim(-0.02,0.0125)
        ax.legend(loc=1,bbox_to_anchor=(1.845, 0.825),ncol=2,frameon=False,fontsize=14.5)

        if not os.path.isdir('Figures/'): os.mkdir('Figures/')
        plt.savefig('Figures/' + semantic_domain + '.png')
        plt.show()

    def cluster_analysis(self):

        self.cross_entropy_matrix_js = self.image_analysis.cross_entropy_matrix_js

        D = np.log2(np.exp(np.matrix(self.cross_entropy_matrix_js)))
        condensedD = squareform(D)

        # Compute and plot first dendrogram.
        fig = plt.figure(figsize=(10,10))
        ax1 = fig.add_axes([0.162,0.1,0.125,0.6])

        Y = sch.linkage(condensedD, method='centroid')
        Z1 = sch.dendrogram(Y, orientation='left', above_threshold_color='dimgrey')

        ax1.set_xticks([])
        ax1.set_yticks([])
        ax1.invert_yaxis()
        ax1.axis('off')

        # Compute and plot second dendrogram.
        ax2 = fig.add_axes([0.3,0.71,0.6,0.125])
        Y = sch.linkage(condensedD, method='centroid')
        Z2 = sch.dendrogram(Y, above_threshold_color='dimgrey')
        ax2.set_xticks([])
        ax2.set_yticks([])
        ax2.axis('off')

        # Plot distance matrix.
        axmatrix = fig.add_axes([0.3,0.1,0.6,0.6])
        idx1 = Z1['leaves']
        idx2 = Z2['leaves']
        D = D[idx1,:]
        D = D[:,idx2]
        im = axmatrix.matshow(D, aspect='auto', origin='lower', cmap=sns.cubehelix_palette(light=1, as_cmap=True, hue=0.),
                             vmin=D.min(),vmax=D.max())
        axmatrix.set_xticks([])
        axmatrix.set_yticks([])

        axmatrix.set_xticks(range(len(self.labels_list)))
        axmatrix.set_xticklabels(np.array(self.labels_list)[idx1], minor=False, fontsize=18)
        axmatrix.xaxis.set_label_position('bottom')
        axmatrix.xaxis.tick_bottom()

        pylab.xticks(rotation=-90)

        axmatrix.set_yticks(range(len(self.labels_list)))
        axmatrix.set_yticklabels(np.array(self.labels_list)[idx2], minor=False, fontsize=18)
        axmatrix.yaxis.set_label_position('right')
        axmatrix.yaxis.tick_right()
        axmatrix.invert_yaxis()

        #Plot colorbar (comment out for matrices without colorbar)
        axcolor = fig.add_axes([1.1,0.1,0.02,0.6])
        cbar = pylab.colorbar(im, cax=axcolor)
        cbar.ax.set_yticks([0,0.005,0.01,0.015,0.02,0.025,0.03])
        cbar.ax.set_yticklabels(['0','','0.01','','0.02','','0.03'],fontsize=12)
        cbar.set_label('Jensen-Shannon Divergence [bits]', labelpad=26,rotation=270, fontsize=18)

        #Colorbars don't mesh well with saving as pdf
        semantic_domain = 'test'
        if not os.path.isdir('Figures/'): os.mkdir('Figures/')
        plt.savefig('Figures/' + semantic_domain + 'dendrogram.png')
        plt.show()

    def plot_tsne(self):

        self.jzazbz_dict_simp = self.image_analysis.jzazbz_dict_simp

        jzbzaz_keys = np.array(list(self.jzazbz_dict_simp.keys()))
        jzbzaz_dists = np.array([np.array(x) for x in self.jzazbz_dict_simp.values()])

        plot_perplexity = 2 #manually set perplexity 
        X_embedded = TSNE(n_components=2,perplexity=plot_perplexity).fit_transform(jzbzaz_dists) #manually set perplexity 

        paths = []
        for key in jzbzaz_keys:
            paths.extend(np.array(['colorgrams/{}'.format(key) + '_colorgram.png']))

        fig, ax = plt.subplots(figsize=(14,14))

        x = X_embedded[:,0]#/np.max(np.abs(X_embedded[:,0]))
        y = X_embedded[:,1]#/np.max(np.abs(X_embedded[:,1]))
        ax.scatter(x,y) 

        for x0, y0, path in zip(x,y,paths):
            ab = AnnotationBbox(getImage(path), (x0, y0), frameon=False)
            ax.add_artist(ab)

        plt.xticks([])
        plt.yticks([])

        plt.xlim(1.1*np.min(x),1.1*np.max(x))
        plt.ylim(1.15*np.min(y),1.15*np.max(y))

        plt.title('t-SNE (perplexity = ' + str(plot_perplexity) + ')',fontsize=20)

        plt.savefig('Figures/tSNE_all_colorgram.pdf')
        plt.show()


