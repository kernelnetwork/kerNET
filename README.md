# kerNET

**Code for paper: 'Learning Backpropagation-Free Deep Architectures with Kernels.'**

Dependencies: 

- PyTorch 1.0
- numpy 1.15
- Python 3.6

To install, do ```python setup.py install```.

------

In examples, we demonstrate training a two-hidden-layer kMLP and a kLeNet-5 (with output layer kernelized) layer-wise for MNIST.

This library itself was built to provide a Keras-like interface for easy implementations of kernel networks and the layer-wise learning method proposed in the paper. It is still under active development and some documentations may be behind the actual code. With that said, the main functions should be pretty self-explanatory.

Thank you and hope you enjoy this repo!

