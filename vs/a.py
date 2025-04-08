import pycuda.autoinit
import pycuda.driver as drv
import numpy
import os
from pycuda.compiler import SourceModule


dirName=os.path.dirname(os.path.abspath(__file__))
print(dirName)
cachePath=os.path.join(dirName, 'cache')

mod = SourceModule("""
#include <stdio.h>

__global__ void multiply_them(float *dest, float *a, float *b)
{
      //printf("I am %d.%d\\n", threadIdx.x, threadIdx.y);
      int cc=10;
      int bb=cc+10;
  const int i = threadIdx.x;
  dest[i] = a[i] * b[i];
}
""", options=['-g','-G'],keep=True,cache_dir=cachePath)

multiply_them = mod.get_function("multiply_them")

a = numpy.random.randn(400).astype(numpy.float32)
b = numpy.random.randn(400).astype(numpy.float32)

dest = numpy.zeros_like(a)
multiply_them(
    drv.Out(dest), drv.In(a), drv.In(b),
    block=(400,1,1), grid=(1,1))

print(dest-a*b)
