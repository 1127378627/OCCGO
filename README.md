# OCCGO

Geometrical Optics with Python-

## Python

* decorate
  * @classmethod
    * instance (function defined in class)
    * need argument like "self"
  * @staticmethod
    * instance (function defined in class) be enable to call
    * Do NOT need argument like "self"
  * @property
    * instance ont\ly to read
    * CANNOT write this value

## Branch

* OCC-18.1
  * pythonocc-core==18.1
    * ONLY windows
    * I CANNOT build pythonocc-core==18.2 in Windows
* OCC-18.2
  * pythonocc-core==18.2
    * Build in linux
  * dealii
    * dealii-6
      * step-6
        * Solve the PDE on the current mesh
        * Estimate the error on each cell using some criterion
        * Mark those cells that have large errors for refinement
        * Mark those cells that have particularly small errors for coarsening
        * Refine and coarsen the cells so marked to obtain a new mesh
        * Repeat the steps above until the overall error is sufficiently small
      * setp-6.1 (step-15)
    * dealii-28
    * dealii-54
    * dealii-61
      * Poisson eq to solve using Weak Galerkin FEM
      * Poisson eq need to satisfy the weak form of probrem
      * Replace the gradient to discrete weak gradient operator
        * discrete approximation
        * value in the interior of cells [ref](https://www.dealii.org/current/doxygen/deal.II/classFE__DGQ.html)
        * value on the interface of cells [ref](https://www.dealii.org/current/doxygen/deal.II/classFE__FaceQ.html)
      * the discrete weak gradient is a lement of Raviart-Thomas space on each cell
        * have continuous normal component at interface between cells
