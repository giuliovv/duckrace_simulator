from numpy import array
from casadi import DM

path = [[0.32, 1.8, -1.47, 0, 0], [0.32, 1.8, -1.48, 0, 0], [0.32, 1.8, -1.5, 0, 0], [0.32, 1.8, -1.44, 0, 0], [0.32, 1.8, -1.45, 0, 0], [0.32, 1.8, -1.46, 0, 0], [0.32, 1.76, -1.46, 0, 0], [0.32, 1.76, -1.46, 0, 0], [0.32, 1.7, -1.58, 0, 0], [0.33, 1.63, -1.57, 0, 0], [0.33, 1.56, -1.53, 0, 0], [0.33, 1.5, -1.5, 0, 0], [0.32, 1.45, -2.0, 0, 0], [0.33, 1.36, -1.51, 0, 0], [0.34, 1.25, -1.42, 0, 0], [0.35, 1.19, -1.27, 0, 0], [0.36, 1.14, -1.27, 0, 0], [0.37, 1.11, -1.22, 0, 0], [0.4, 1.02, -1.12, 0, 0], [0.43, 0.95, -1.09, 0, 0], [0.47, 0.86, -1.18, 0, 0], [0.5, 0.78, -1.21, 0, 0], [0.51, 0.74, -1.32, 0, 0], [0.53, 0.66, -1.44, 0, 0], [0.54, 0.6, -1.4, 0, 0], [0.54, 0.52, -1.26, 0, 0], [0.53, 0.48, -0.72, 0, 0], [0.54, 0.45, -0.24, 0, 0], [0.55, 0.43, -0.01, 0, 0], [0.6, 0.43, -0.01, 0, 0], [0.64, 0.44, -0.01, 0, 0], [0.73, 0.46, -0.01, 0, 0], [0.8, 0.47, -0.01, 0, 0], [0.87, 0.48, -0.01, 0, 0], [0.95, 0.49, -0.01, 0, 0], [1.02, 0.5, -0.01, 0, 0], [1.09, 0.51, -0.01, 0, 0], [1.13, 0.52, -0.01, 0, 0], [1.18, 0.53, -0.01, 0, 0], [1.27, 0.54, -0.01, 0, 0], [1.3, 0.56, -0.01, 0, 0], [1.35, 0.57, -0.01, 0, 0], [1.44, 0.59, -0.01, 0, 0], [1.52, 0.62, -0.01, 0, 0], [1.58, 0.63, -0.01, 0, 0], [1.6, 0.63, -0.01, 0, 0], [1.63, 0.65, -0.01, 0, 0], [1.65, 0.66, 1.64, 0, 0], [1.66, 0.67, 1.94, 0, 0], [1.67, 0.68, 2.09, 0, 0], [1.66, 0.69, 2.1, 0, 0], [1.65, 0.72, 2.15, 0, 0], [1.61, 0.8, 2.12, 0, 0], [1.59, 0.85, 2.01, 0, 0], [1.56, 0.94, 1.96, 0, 0], [1.54, 0.97, 1.83, 0, 0], [1.53, 1.01, 1.76, 0, 0], [1.53, 1.04, 1.61, 0, 0], [1.52, 1.11, 1.37, 0, 0], [1.54, 1.16, 1.14, 0, 0], [1.56, 1.22, 1.11, 0, 0], [1.59, 1.27, 1.03, 0, 0], [1.62, 1.32, 0.93, 0, 0], [1.65, 1.37, 0.89, 0, 0], [1.68, 1.42, 0.9, 0, 0], [1.73, 1.47, 0.8, 0, 0], [1.77, 1.52, 0.74, 0, 0], [1.81, 1.56, 0.66, 0, 0], [1.84, 1.58, 0.67, 0, 0], [1.86, 1.6, 0.6, 0, 0], [1.94, 1.65, 0.34, 0, 0], [1.98, 1.67, 0.23, 0, 0], [2.03, 1.69, 0.1, 0, 0], [2.08, 1.7, 0.1, 0, 0], [2.13, 1.69, 0.36, 0, 0], [2.15, 1.69, 0.76, 0, 0], [2.18, 1.7, 1.23, 0, 0], [2.18, 1.71, 1.39, 0, 0], [2.19, 1.74, 1.57, 0, 0], [2.19, 1.76, 1.6, 0, 0], [2.19, 1.76, 1.6, 0, 0], [2.18, 1.9, 1.74, 0.20320798440800003, 0.09466662979599999], [2.18, 1.96, 1.79, 0.20320798440800003, 0.09466662979599999], [2.17, 2.02, 1.82, 0.20320798440800003, 0.09466662979599999], [2.16, 2.06, 1.81, 0.20320798440800003, 0.09466662979599999], [2.16, 2.11, 1.84, 0.20320798440800003, 0.09466662979599999], [2.15, 2.13, 1.82, 0.20320798440800003, 0.09466662979599999], [2.14, 2.21, 1.94, 0.20320798440800003, 0.09466662979599999], [2.11, 2.28, 2.0, 0.20320798440800003, 0.09466662979599999], [2.11, 2.31, 1.96, 0.20320798440800003, 0.09466662979599999], [2.09, 2.36, 1.94, 0.20320798440800003, 0.09466662979599999], [2.08, 2.4, 1.97, 0.20320798440800003, 0.09466662979599999], [2.07, 2.43, 2.11, 0.20320798440800003, 0.09466662979599999], [2.06, 2.44, 2.11, 0.20320798440800003, 0.09466662979599999], [2.05, 2.47, 2.21, 0.20320798440800003, 0.09466662979599999], [2.05, 2.5, 2.54, 0.20320798440800003, 0.09466662979599999], [2.01, 2.53, 2.75, 0.20320798440800003, 0.09466662979599999], [1.98, 2.55, 2.88, 0.20320798440800003, 0.09466662979599999], [1.95, 2.57, 2.96, 0.20320798440800003, 0.09466662979599999], [1.9, 2.58, 3.08, 0.20320798440800003, 0.09466662979599999], [1.86, 2.58, 3.07, 0.20320798440800003, 0.09466662979599999], [1.81, 2.59, 3.09, 0.20320798440800003, 0.09466662979599999], [1.73, 2.6, 3.07, 0.20320798440800003, 0.09466662979599999], [1.7, 2.6, 3.07, 0.20320798440800003, 0.09466662979599999], [1.63, 2.61, 3.0, 0.20320798440800003, 0.09466662979599999], [1.58, 2.61, 2.79, 0.20320798440800003, 0.09466662979599999], [1.56, 2.62, 2.79, 0.20320798440800003, 0.09466662979599999], [1.5, 2.63, 2.22, 0.20320798440800003, 0.09466662979599999], [1.48, 2.64, 1.75, 0.20320798440800003, 0.09466662979599999], [1.47, 2.66, 1.36, 0.20320798440800003, 0.09466662979599999], [1.47, 2.67, 1.32, 0.20320798440800003, 0.09466662979599999], [1.48, 2.72, 1.36, 0.20320798440800003, 0.09466662979599999], [1.5, 2.76, 1.44, 0.20320798440800003, 0.09466662979599999], [1.51, 2.8, 1.62, 0.20320798440800003, 0.09466662979599999], [1.52, 2.81, 2.05, 0.20320798440800003, 0.09466662979599999], [1.54, 2.83, 2.63, 0.20320798440800003, 0.09466662979599999], [1.54, 2.84, 2.79, 0.20320798440800003, 0.09466662979599999], [1.5, 2.86, 3.06, 0.20320798440800003, 0.09466662979599999], [1.48, 2.87, 3.05, 0.20320798440800003, 0.09466662979599999], [1.43, 2.87, 3.01, 0.20320798440800003, 0.09466662979599999], [1.39, 2.88, 2.96, 0.20320798440800003, 0.09466662979599999], [1.35, 2.89, 2.8, 0.20320798440800003, 0.09466662979599999], [1.32, 2.9, 2.8, 0.20320798440800003, 0.09466662979599999], [1.28, 2.91, 2.8, 0.20320798440800003, 0.09466662979599999], [1.26, 2.92, 2.79, 0.20320798440800003, 0.09466662979599999], [1.21, 2.95, 2.65, 0.20320798440800003, 0.09466662979599999], [1.16, 2.98, 2.61, 0.20320798440800003, 0.09466662979599999], [1.13, 3.0, 2.68, 0.20320798440800003, 0.09466662979599999], [1.1, 3.02, 2.77, 0.20320798440800003, 0.09466662979599999], [1.05, 3.07, 2.94, 0.20320798440800003, 0.09466662979599999], [1.01, 3.09, 2.92, 0.20320798440800003, 0.09466662979599999], [0.97, 3.11, 2.94, 0.20320798440800003, 0.09466662979599999], [0.94, 3.13, 2.87, 0.20320798440800003, 0.09466662979599999], [0.89, 3.14, 2.87, 0.20320798440800003, 0.09466662979599999], [0.86, 3.15, 2.9, 0.20320798440800003, 0.09466662979599999], [0.83, 3.15, 2.95, 0.20320798440800003, 0.09466662979599999], [0.81, 3.16, 3.05, 0.20320798440800003, 0.09466662979599999], [0.77, 3.17, 3.1, 0.20320798440800003, 0.09466662979599999], [0.74, 3.18, -3.12, 0.20320798440800003, 0.09466662979599999], [0.7, 3.18, -2.98, 0.20320798440800003, 0.09466662979599999], [0.66, 3.18, -2.94, 0.20320798440800003, 0.09466662979599999], [0.61, 3.17, -2.83, 0.20320798440800003, 0.09466662979599999], [0.6, 3.16, -2.79, 0.20320798440800003, 0.09466662979599999], [0.56, 3.15, -2.73, 0.20320798440800003, 0.09466662979599999], [0.51, 3.12, -2.62, 0.20320798440800003, 0.09466662979599999], [0.45, 3.09, -2.56, 0.20320798440800003, 0.09466662979599999], [0.45, 3.09, -2.56, 0.20320798440800003, 0.09466662979599999], [0.38, 3.04, -2.41, 0.2640624476946147, 0.2890011321510428], [0.33, 3.01, -2.17, 0.2640624476946147, 0.2890011321510428], [0.32, 2.99, -2.15, 0.2640624476946147, 0.2890011321510428], [0.28, 2.95, -1.94, 0.2640624476946147, 0.2890011321510428], [0.27, 2.91, -1.77, 0.2640624476946147, 0.2890011321510428], [0.27, 2.9, -1.84, 0.2640624476946147, 0.2890011321510428], [0.26, 2.87, -1.63, 0.2640624476946147, 0.2890011321510428], [0.25, 2.83, -1.5, 0.2640624476946147, 0.2890011321510428], [0.24, 2.79, -1.45, 0.2640624476946147, 0.2890011321510428], [0.24, 2.77, -1.36, 0.2640624476946147, 0.2890011321510428], [0.25, 2.7, -1.29, 0.2640624476946147, 0.2890011321510428], [0.26, 2.65, -1.25, 0.2640624476946147, 0.2890011321510428], [0.27, 2.62, -1.29, 0.2640624476946147, 0.2890011321510428], [0.29, 2.56, -1.23, 0.2640624476946147, 0.2890011321510428], [0.3, 2.52, -1.23, 0.2640624476946147, 0.2890011321510428], [0.31, 2.49, -1.31, 0.2640624476946147, 0.2890011321510428], [0.32, 2.46, -1.38, 0.2640624476946147, 0.2890011321510428], [0.32, 2.42, -1.55, 0.2640624476946147, 0.2890011321510428], [0.33, 2.38, -1.61, 0.2640624476946147, 0.2890011321510428], [0.33, 2.36, -1.64, 0.2640624476946147, 0.2890011321510428], [0.33, 2.31, -1.71, 0.2640624476946147, 0.2890011321510428], [0.32, 2.3, -1.72, 0.2640624476946147, 0.2890011321510428], [0.32, 2.25, -1.73, 0.2640624476946147, 0.2890011321510428], [0.31, 2.23, -1.67, 0.2640624476946147, 0.2890011321510428], [0.31, 2.23, -1.67, 0.2640624476946147, 0.2890011321510428], [0.31, 2.16, -1.72, 0.2743263420828265, 0.2262290443439793], [0.3, 2.13, -1.65, 0.2743263420828265, 0.2262290443439793], [0.3, 2.09, -1.6, 0.2743263420828265, 0.2262290443439793], [0.3, 2.06, -1.67, 0.2743263420828265, 0.2262290443439793], [0.3, 2.04, -1.69, 0.2743263420828265, 0.2262290443439793], [0.29, 2.01, -1.77, 0.2743263420828265, 0.2262290443439793], [0.29, 2.0, -1.75, 0.2743263420828265, 0.2262290443439793], [0.29, 1.97, -1.78, 0.2743263420828265, 0.2262290443439793], [0.29, 1.95, -1.74, 0.2743263420828265, 0.2262290443439793], [0.27, 1.9, -1.59, 0.2743263420828265, 0.2262290443439793], [0.27, 1.87, -1.53, 0.2743263420828265, 0.2262290443439793], [0.27, 1.82, -1.35, 0.2743263420828265, 0.2262290443439793], [0.28, 1.8, -1.32, 0.2743263420828265, 0.2262290443439793], [0.28, 1.76, -1.3, 0.2743263420828265, 0.2262290443439793], [0.3, 1.69, -1.3, 0.2743263420828265, 0.2262290443439793], [0.31, 1.64, -1.31, 0.2743263420828265, 0.2262290443439793], [0.32, 1.6, -1.31, 0.2743263420828265, 0.2262290443439793], [0.34, 1.55, -1.22, 0.2743263420828265, 0.2262290443439793], [0.35, 1.5, -1.22, 0.2743263420828265, 0.2262290443439793], [0.37, 1.45, -1.33, 0.2743263420828265, 0.2262290443439793], [0.37, 1.43, -1.33, 0.2743263420828265, 0.2262290443439793], [0.39, 1.39, -1.37, 0.2743263420828265, 0.2262290443439793], [0.4, 1.36, -1.45, 0.2743263420828265, 0.2262290443439793], [0.4, 1.31, -1.57, 0.2743263420828265, 0.2262290443439793], [0.41, 1.29, -1.62, 0.2743263420828265, 0.2262290443439793], [0.4, 1.18, -1.78, 0.2743263420828265, 0.2262290443439793], [0.4, 1.17, -1.84, 0.2743263420828265, 0.2262290443439793], [0.39, 1.11, -1.87, 0.2743263420828265, 0.2262290443439793], [0.38, 1.06, -1.88, 0.2743263420828265, 0.2262290443439793], [0.36, 1.02, -1.82, 0.2743263420828265, 0.2262290443439793], [0.36, 1.02, -1.81, 0.2743263420828265, 0.2262290443439793], [0.34, 0.93, -1.63, 0.2743263420828265, 0.2262290443439793], [0.34, 0.92, -1.61, 0.2743263420828265, 0.2262290443439793], [0.33, 0.87, -1.5, 0.2743263420828265, 0.2262290443439793], [0.33, 0.82, -1.4, 0.2743263420828265, 0.2262290443439793], [0.33, 0.79, -1.29, 0.2743263420828265, 0.2262290443439793], [0.34, 0.74, -1.12, 0.2743263420828265, 0.2262290443439793], [0.36, 0.69, -0.96, 0.2743263420828265, 0.2262290443439793], [0.38, 0.64, -0.78, 0.2743263420828265, 0.2262290443439793], [0.41, 0.61, -0.59, 0.2743263420828265, 0.2262290443439793], [0.45, 0.57, -0.33, 0.2743263420828265, 0.2262290443439793], [0.48, 0.55, -0.25, 0.2743263420828265, 0.2262290443439793], [0.56, 0.53, -0.09, 0.2743263420828265, 0.2262290443439793], [0.64, 0.51, -0.05, 0.2743263420828265, 0.2262290443439793], [0.7, 0.52, 0.06, 0.2743263420828265, 0.2262290443439793], [0.75, 0.51, 0.15, 0.2743263420828265, 0.2262290443439793], [0.8, 0.52, 0.17, 0.2743263420828265, 0.2262290443439793], [0.83, 0.52, 0.19, 0.2743263420828265, 0.2262290443439793], [0.83, 0.52, 0.19, 0.2743263420828265, 0.2262290443439793], [0.95, 0.55, 0.3, 0.2743263420828265, 0.2262290443439793], [1.01, 0.57, 0.32, 0.2743263420828265, 0.2262290443439793], [1.06, 0.59, 0.37, 0.2743263420828265, 0.2262290443439793], [1.12, 0.61, 0.37, 0.2743263420828265, 0.2262290443439793], [1.18, 0.64, 0.33, 0.2743263420828265, 0.2262290443439793], [1.26, 0.67, 0.26, 0.2743263420828265, 0.2262290443439793], [1.3, 0.68, 0.23, 0.2743263420828265, 0.2262290443439793], [1.36, 0.69, 0.16, 0.2743263420828265, 0.2262290443439793], [1.42, 0.71, 0.19, 0.2743263420828265, 0.2262290443439793], [1.45, 0.71, 0.2, 0.2743263420828265, 0.2262290443439793], [1.52, 0.72, 0.23, 0.2743263420828265, 0.2262290443439793], [1.6, 0.73, 0.36, 0.2743263420828265, 0.2262290443439793], [1.63, 0.74, 0.41, 0.2743263420828265, 0.2262290443439793], [1.66, 0.74, 0.9, 0.2743263420828265, 0.2262290443439793], [1.68, 0.74, 1.26, 0.2743263420828265, 0.2262290443439793], [1.7, 0.75, 1.57, 0.2743263420828265, 0.2262290443439793], [1.7, 0.76, 1.65, 0.2743263420828265, 0.2262290443439793], [1.7, 0.8, 1.74, 0.2743263420828265, 0.2262290443439793], [1.69, 0.85, 1.79, 0.2743263420828265, 0.2262290443439793], [1.69, 0.9, 1.69, 0.2743263420828265, 0.2262290443439793], [1.69, 0.97, 1.55, 0.2743263420828265, 0.2262290443439793], [1.68, 1.01, 1.56, 0.2743263420828265, 0.2262290443439793], [1.69, 1.07, 1.54, 0.2743263420828265, 0.2262290443439793], [1.69, 1.11, 1.52, 0.2743263420828265, 0.2262290443439793], [1.69, 1.16, 1.45, 0.2743263420828265, 0.2262290443439793], [1.7, 1.2, 1.24, 0.2743263420828265, 0.2262290443439793], [1.7, 1.24, 1.18, 0.2743263420828265, 0.2262290443439793], [1.71, 1.29, 0.77, 0.2743263420828265, 0.2262290443439793], [1.73, 1.32, 0.38, 0.2743263420828265, 0.2262290443439793], [1.74, 1.33, 0.12, 0.2743263420828265, 0.2262290443439793], [1.75, 1.34, 0.06, 0.2743263420828265, 0.2262290443439793], [1.8, 1.34, 0.19, 0.2743263420828265, 0.2262290443439793], [1.84, 1.32, 0.28, 0.2743263420828265, 0.2262290443439793], [1.9, 1.31, 0.42, 0.2743263420828265, 0.2262290443439793], [1.95, 1.3, 0.51, 0.2743263420828265, 0.2262290443439793], [2.0, 1.29, 0.05, 0.2743263420828265, 0.2262290443439793], [2.06, 1.3, 0.21, 0.2743263420828265, 0.2262290443439793], [2.11, 1.29, 0.59, 0.2743263420828265, 0.2262290443439793], [2.13, 1.29, 1.02, 0.2743263420828265, 0.2262290443439793], [2.15, 1.3, 1.42, 0.2743263420828265, 0.2262290443439793], [2.17, 1.32, 1.91, 0.2743263420828265, 0.2262290443439793], [2.16, 1.34, 2.17, 0.2743263420828265, 0.2262290443439793], [2.14, 1.37, 2.19, 0.2743263420828265, 0.2262290443439793], [2.14, 1.37, 2.19, 0.2743263420828265, 0.2262290443439793], [2.11, 1.43, 2.11, 0.2743263420828265, 0.2262290443439793], [2.08, 1.48, 1.93, 0.2743263420828265, 0.2262290443439793], [2.07, 1.51, 1.82, 0.2743263420828265, 0.2262290443439793], [2.05, 1.57, 1.38, 0.2743263420828265, 0.2262290443439793], [2.05, 1.58, 1.12, 0.2743263420828265, 0.2262290443439793], [2.05, 1.59, 0.91, 0.2743263420828265, 0.2262290443439793], [2.06, 1.61, 0.91, 0.2743263420828265, 0.2262290443439793], [2.09, 1.66, 0.91, 0.2743263420828265, 0.2262290443439793], [2.12, 1.69, 0.99, 0.2743263420828265, 0.2262290443439793], [2.15, 1.73, 1.02, 0.2743263420828265, 0.2262290443439793], [2.17, 1.76, 1.28, 0.2743263420828265, 0.2262290443439793], [2.19, 1.78, 1.79, 0.2743263420828265, 0.2262290443439793], [2.2, 1.79, 1.94, 0.2743263420828265, 0.2262290443439793], [2.19, 1.81, 2.04, 0.2743263420828265, 0.2262290443439793], [2.18, 1.84, 1.97, 0.2743263420828265, 0.2262290443439793], [2.17, 1.88, 1.95, 0.2743263420828265, 0.2262290443439793], [2.16, 1.92, 1.89, 0.2743263420828265, 0.2262290443439793], [2.15, 1.94, 1.8, 0.2743263420828265, 0.2262290443439793], [2.14, 2.01, 1.73, 0.2743263420828265, 0.2262290443439793], [2.14, 2.02, 1.67, 0.2743263420828265, 0.2262290443439793], [2.13, 2.08, 1.63, 0.2743263420828265, 0.2262290443439793], [2.13, 2.1, 1.66, 0.2743263420828265, 0.2262290443439793], [2.13, 2.16, 1.61, 0.2743263420828265, 0.2262290443439793], [2.13, 2.2, 1.65, 0.2743263420828265, 0.2262290443439793], [2.13, 2.22, 1.6, 0.2743263420828265, 0.2262290443439793], [2.13, 2.28, 1.71, 0.2743263420828265, 0.2262290443439793], [2.13, 2.32, 1.78, 0.2743263420828265, 0.2262290443439793], [2.13, 2.34, 1.84, 0.2743263420828265, 0.2262290443439793], [2.12, 2.39, 1.97, 0.2743263420828265, 0.2262290443439793], [2.12, 2.42, 2.51, 0.2743263420828265, 0.2262290443439793], [2.11, 2.43, 2.76, 0.2743263420828265, 0.2262290443439793], [2.09, 2.46, -3.11, 0.2743263420828265, 0.2262290443439793], [2.09, 2.46, -3.11, 0.2743263420828265, 0.2262290443439793], [2.05, 2.47, -2.83, 0.32045346942041414, -0.006923984319952808], [1.97, 2.44, -2.84, 0.32045346942041414, -0.006923984319952808], [1.94, 2.42, -3.0, 0.32045346942041414, -0.006923984319952808], [1.89, 2.42, -3.07, 0.32045346942041414, -0.006923984319952808], [1.87, 2.4, 2.91, 0.32045346942041414, -0.006923984319952808], [1.86, 2.4, 2.72, 0.32045346942041414, -0.006923984319952808], [1.86, 2.4, 2.72, 0.32045346942041414, -0.006923984319952808], [1.79, 2.44, 2.38, 0.32045346942041414, -0.006923984319952808], [1.79, 2.44, 2.38, 0.32045346942041414, -0.006923984319952808], [1.76, 2.48, 2.27, 0.32045346942041414, -0.006923984319952808], [1.73, 2.52, 2.3, 0.32045346942041414, -0.006923984319952808], [1.7, 2.56, 2.33, 0.32045346942041414, -0.006923984319952808], [1.69, 2.58, 2.31, 0.32045346942041414, -0.006923984319952808], [1.64, 2.65, 2.41, 0.32045346942041414, -0.006923984319952808], [1.62, 2.67, 2.46, 0.32045346942041414, -0.006923984319952808], [1.6, 2.7, 2.44, 0.32045346942041414, -0.006923984319952808], [1.56, 2.73, 2.42, 0.32045346942041414, -0.006923984319952808], [1.54, 2.75, 2.45, 0.32045346942041414, -0.006923984319952808], [1.52, 2.77, 2.38, 0.32045346942041414, -0.006923984319952808], [1.51, 2.79, 2.39, 0.32045346942041414, -0.006923984319952808], [1.49, 2.81, 2.41, 0.32045346942041414, -0.006923984319952808], [1.49, 2.81, 2.41, 0.32045346942041414, -0.006923984319952808], [1.45, 2.86, 2.43, 0.29643959228746664, 0.08038795319411692], [1.42, 2.88, 2.58, 0.29643959228746664, 0.08038795319411692], [1.4, 2.9, 2.65, 0.29643959228746664, 0.08038795319411692], [1.4, 2.9, 2.65, 0.29643959228746664, 0.08038795319411692], [1.36, 2.93, 2.65, 0.3089084351833464, 0.09121701625251191], [1.33, 2.96, 2.66, 0.3089084351833464, 0.09121701625251191], [1.28, 2.98, 2.75, 0.3089084351833464, 0.09121701625251191], [1.24, 3.01, 2.8, 0.3089084351833464, 0.09121701625251191], [1.22, 3.02, 2.82, 0.3089084351833464, 0.09121701625251191], [1.16, 3.07, -3.08, 0.3089084351833464, 0.09121701625251191], [1.13, 3.07, 3.02, 0.3089084351833464, 0.09121701625251191], [1.09, 3.1, -3.02, 0.3089084351833464, 0.09121701625251191], [1.06, 3.1, -3.04, 0.3089084351833464, 0.09121701625251191], [1.02, 3.12, -3.11, 0.3089084351833464, 0.09121701625251191], [0.95, 3.12, -3.13, 0.3089084351833464, 0.09121701625251191], [0.9, 3.13, 3.09, 0.3089084351833464, 0.09121701625251191], [0.84, 3.14, -3.12, 0.3089084351833464, 0.09121701625251191], [0.8, 3.13, 3.12, 0.3089084351833464, 0.09121701625251191], [0.74, 3.13, -3.07, 0.3089084351833464, 0.09121701625251191], [0.7, 3.13, -2.96, 0.3089084351833464, 0.09121701625251191], [0.67, 3.13, -2.91, 0.3089084351833464, 0.09121701625251191], [0.61, 3.12, -2.81, 0.3089084351833464, 0.09121701625251191], [0.59, 3.11, -2.74, 0.3089084351833464, 0.09121701625251191], [0.53, 3.1, -2.63, 0.3089084351833464, 0.09121701625251191], [0.52, 3.09, -2.57, 0.3089084351833464, 0.09121701625251191], [0.45, 3.04, -2.31, 0.3089084351833464, 0.09121701625251191], [0.42, 3.02, -2.24, 0.3089084351833464, 0.09121701625251191], [0.4, 3.0, -2.03, 0.3089084351833464, 0.09121701625251191], [0.4, 3.0, -2.03, 0.3089084351833464, 0.09121701625251191], [0.37, 2.96, -1.92, 0.3089084351833464, 0.09121701625251191], [0.36, 2.93, -1.88, 0.3089084351833464, 0.09121701625251191], [0.35, 2.9, -1.84, 0.3089084351833464, 0.09121701625251191], [0.34, 2.86, -1.7, 0.3089084351833464, 0.09121701625251191], [0.33, 2.84, -1.69, 0.3089084351833464, 0.09121701625251191], [0.33, 2.8, -1.73, 0.3089084351833464, 0.09121701625251191], [0.32, 2.76, -1.62, 0.3089084351833464, 0.09121701625251191], [0.32, 2.73, -1.5, 0.3089084351833464, 0.09121701625251191], [0.32, 2.7, -1.56, 0.3089084351833464, 0.09121701625251191], [0.32, 2.68, -1.6, 0.3089084351833464, 0.09121701625251191], [0.33, 2.65, -1.6, 0.3089084351833464, 0.09121701625251191], [0.33, 2.63, -1.74, 0.3089084351833464, 0.09121701625251191], [0.32, 2.6, -1.75, 0.3089084351833464, 0.09121701625251191], [0.32, 2.57, -1.65, 0.3089084351833464, 0.09121701625251191], [0.32, 2.54, -1.68, 0.3089084351833464, 0.09121701625251191], [0.31, 2.52, -1.57, 0.3089084351833464, 0.09121701625251191], [0.31, 2.5, -1.61, 0.3089084351833464, 0.09121701625251191], [0.31, 2.47, -1.6, 0.3089084351833464, 0.09121701625251191], [0.31, 2.44, -1.63, 0.3089084351833464, 0.09121701625251191], [0.31, 2.42, -1.59, 0.3089084351833464, 0.09121701625251191], [0.3, 2.4, -1.61, 0.3089084351833464, 0.09121701625251191], [0.3, 2.37, -1.67, 0.3089084351833464, 0.09121701625251191], [0.3, 2.36, -1.64, 0.3089084351833464, 0.09121701625251191], [0.3, 2.33, -1.69, 0.3089084351833464, 0.09121701625251191], [0.3, 2.31, -1.6, 0.3089084351833464, 0.09121701625251191], [0.29, 2.27, -1.53, 0.3089084351833464, 0.09121701625251191], [0.29, 2.25, -1.55, 0.3089084351833464, 0.09121701625251191], [0.3, 2.24, -1.47, 0.3089084351833464, 0.09121701625251191], [0.3, 2.2, -1.44, 0.3089084351833464, 0.09121701625251191], [0.3, 2.18, -1.41, 0.3089084351833464, 0.09121701625251191], [0.3, 2.16, -1.44, 0.3089084351833464, 0.09121701625251191], [0.31, 2.13, -1.44, 0.3089084351833464, 0.09121701625251191], [0.31, 2.1, -1.4, 0.3089084351833464, 0.09121701625251191], [0.31, 2.08, -1.44, 0.3089084351833464, 0.09121701625251191], [0.31, 2.05, -1.43, 0.3089084351833464, 0.09121701625251191], [0.32, 2.03, -1.47, 0.3089084351833464, 0.09121701625251191], [0.32, 2.0, -1.48, 0.3089084351833464, 0.09121701625251191], [0.32, 1.96, -1.51, 0.3089084351833464, 0.09121701625251191], [0.32, 1.93, -1.47, 0.3089084351833464, 0.09121701625251191], [0.33, 1.91, -1.49, 0.3089084351833464, 0.09121701625251191], [0.33, 1.87, -1.45, 0.3089084351833464, 0.09121701625251191], [0.34, 1.84, -1.45, 0.3089084351833464, 0.09121701625251191], [0.33, 1.83, -1.42, 0.3089084351833464, 0.09121701625251191], [0.34, 1.81, -1.47, 0.3089084351833464, 0.09121701625251191], [0.34, 1.76, -1.52, 0.3089084351833464, 0.09121701625251191], [0.35, 1.71, -1.55, 0.3089084351833464, 0.09121701625251191], [0.35, 1.68, -1.54, 0.3089084351833464, 0.09121701625251191], [0.35, 1.62, -1.57, 0.3089084351833464, 0.09121701625251191], [0.35, 1.56, -1.58, 0.3089084351833464, 0.09121701625251191], [0.35, 1.49, -1.61, 0.3089084351833464, 0.09121701625251191], [0.35, 1.39, -1.77, 0.3089084351833464, 0.09121701625251191], [0.36, 1.36, -1.88, 0.3089084351833464, 0.09121701625251191], [0.33, 1.29, -2.06, 0.3089084351833464, 0.09121701625251191], [0.32, 1.25, -2.12, 0.3089084351833464, 0.09121701625251191], [0.33, 1.25, -2.24, 0.3089084351833464, 0.09121701625251191], [0.31, 1.23, -2.25, 0.3089084351833464, 0.09121701625251191], [0.29, 1.19, -2.25, 0.3089084351833464, 0.09121701625251191], [0.27, 1.16, -2.31, 0.3089084351833464, 0.09121701625251191], [0.26, 1.15, -2.37, 0.3089084351833464, 0.09121701625251191], [0.16, 1.05, -2.46, 0.3089084351833464, 0.09121701625251191], [0.14, 1.03, -2.5, 0.3089084351833464, 0.09121701625251191], [0.04, 0.95, -2.46, 0.3089084351833464, 0.09121701625251191], [0.05, 0.96, -2.47, 0.3089084351833464, 0.09121701625251191], [0.06, 0.97, -2.49, 0.3089084351833464, 0.09121701625251191], [0.07, 0.98, -2.4, 0.3089084351833464, 0.09121701625251191], [0.07, 0.98, -2.42, 0.3089084351833464, 0.09121701625251191], [0.07, 0.98, -2.41, 0.3089084351833464, 0.09121701625251191], [0.07, 0.98, -2.41, 0.3089084351833464, 0.09121701625251191], [0.07, 0.98, -2.42, 0.3089084351833464, 0.09121701625251191], [0.07, 0.98, -2.41, 0.3089084351833464, 0.09121701625251191], [0.07, 0.98, -2.42, 0.3089084351833464, 0.09121701625251191], [0.07, 0.98, -2.41, 0.3089084351833464, 0.09121701625251191]]
reference =  [array([ 0.32,  1.45, -2.  ,  0.  ,  0.  ]), array([ 0.34      ,  1.55      , -1.22      ,  0.27432634,  0.22622904]), array([ 0.35,  1.19, -1.27,  0.  ,  0.  ]), array([ 0.34      ,  1.55      , -1.22      ,  0.27432634,  0.22622904]), array([ 0.37,  1.11, -1.22,  0.  ,  0.  ]), array([ 0.34,  1.25, -1.42,  0.  ,  0.  ]), array([ 0.43,  0.95, -1.09,  0.  ,  0.  ]), array([ 0.37,  1.11, -1.22,  0.  ,  0.  ]), array([ 0.5 ,  0.78, -1.21,  0.  ,  0.  ]), array([ 0.4 ,  1.02, -1.12,  0.  ,  0.  ]), array([ 0.51,  0.74, -1.32,  0.  ,  0.  ]), array([ 0.51,  0.74, -1.32,  0.  ,  0.  ]), array([ 0.51,  0.74, -1.32,  0.  ,  0.  ]), array([ 0.53,  0.66, -1.44,  0.  ,  0.  ]), array([ 0.53,  0.66, -1.44,  0.  ,  0.  ]), array([ 0.47,  0.86, -1.18,  0.  ,  0.  ]), array([ 0.54,  0.6 , -1.4 ,  0.  ,  0.  ]), array([ 0.5 ,  0.78, -1.21,  0.  ,  0.  ]), array([ 0.54,  0.6 , -1.4 ,  0.  ,  0.  ]), array([ 0.5 ,  0.78, -1.21,  0.  ,  0.  ]), array([ 0.54,  0.52, -1.26,  0.  ,  0.  ]), array([ 0.54,  0.6 , -1.4 ,  0.  ,  0.  ]), array([ 0.54,  0.52, -1.26,  0.  ,  0.  ]), array([ 0.5 ,  0.78, -1.21,  0.  ,  0.  ]), array([ 0.54,  0.52, -1.26,  0.  ,  0.  ]), array([ 0.51,  0.74, -1.32,  0.  ,  0.  ]), array([ 0.5 ,  0.78, -1.21,  0.  ,  0.  ]), array([ 0.54,  0.52, -1.26,  0.  ,  0.  ])]
params =  {'N': 4, 'K': 5, 'Qx': 1000.0, 'Qy': 1000.0, 'Qt': 10.0, 'Qv': 0, 'Qw': 1, 'Ql': 1000.0, 'Q2': 10000.0, 'Q3': 0}
chosen_ref =  [DM([0.354373, 1.61078, -1.61078, -9.99587e-09, -8.24331e-09]), DM([0.3356, 1.561, -1.2398, 0.274326, 0.226229]), DM([0.3714, 1.53062, -1.69944, 0, 0]), DM([0.351075, 1.50204, -1.42463, 0.144535, 0.119194]), DM([0.350844, 1.28987, -1.46529, 0, 0]), DM([0.347141, 1.39857, -1.43287, 0.117553, 0.0969429]), DM([0.4, 1.02, -1.12, 0, 0]), DM([0.34, 1.25, -1.42, 0, 0]), DM([0.43, 0.95, -1.09, 0, 0]), DM([0.36, 1.14, -1.27, 0, 0]), DM([0.47, 0.86, -1.18, 0, 0]), DM([0.47, 0.86, -1.18, 0, 0]), DM([0.47, 0.86, -1.18, 0, 0]), DM([0.5, 0.78, -1.21, 0, 0]), DM([0.5, 0.78, -1.21, 0, 0]), DM([0.407416, 1.00112, -1.13348, 0, 0]), DM([0.51, 0.74, -1.32, 0, 0]), DM([0.446854, 0.901123, -1.14899, 0, 0]), DM([0.53, 0.66, -1.44, 0, 0]), DM([0.439341, 0.922912, -1.12269, 0, 0]), DM([0.54, 0.6, -1.4, 0, 0]), DM([0.51, 0.74, -1.32, 0, 0]), DM([0.54, 0.6, -1.4, 0, 0]), DM([0.437503, 0.928242, -1.11626, 0, 0]), DM([0.54, 0.6, -1.4, 0, 0]), DM([0.47, 0.86, -1.18, 0, 0]), DM([0.437308, 0.928808, -1.11558, 0, 0]), DM([0.54, 0.6, -1.4, 0, 0])]