/home/google/.local/lib/python3.10/site-packages/pycuda/compiler.py

```
    from tempfile import mkdtemp

    #file_dir = mkdtemp()
    #file_dir = mkdtemp(prefix="/home/google/CLionProjects/CUDAClionStarterProject/vs/tmp")
    print("cache_dir")
    print(cache_dir)
    file_dir = "/home/google/CLionProjects/CUDAClionStarterProject/vs/cache/tmp"
    file_root = "kernel"
```

clion
File | Settings | Build, Execution, Deployment
CMake| Debug | CMake options:
新增一行
```

-DCMAKE_CUDA_COMPILER=/usr/local/cuda-12.2/bin/nvcc
```
