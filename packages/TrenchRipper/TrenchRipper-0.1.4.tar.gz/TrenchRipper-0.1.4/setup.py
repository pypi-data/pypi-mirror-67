import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='TrenchRipper',
    version='0.1.4',
    author="Daniel Eaton",
    packages=setuptools.find_packages(),
    install_requires=[
        'pandas==1.0.3',
        'numpy>=1.18.1',
        'h5py>=2.10.0',
        'h5py-cache==1.0',
        'scipy>=1.4.1',
        'scikit-image>=0.16.2',
        'jupyter-client==6.1.3',
        'jupyter-core==4.6.3',
        'jupyterlab==2.0.1',
        'jupyterlab-server==1.0.7',
        'jupyter-server-proxy==1.3.2',
        'matplotlib',
        'dask[complete]==2.12.0',
        'dask-jobqueue==0.7.0',
        'dask-labextension==2.0.1',
        'tifffile>=2020.2.16',
        'ipywidgets==7.5.1',
        'pulp>=1.6.8',
        'fastparquet>=0.3.3',
#         'torch>=1.4.0',
#         'torchvision>=0.5.0',
        'tables>=3.6.1',
        'scikit-learn>=0.22.1',
        'seaborn==0.10.0',
        'h5py_cache==1.0',
        'nd2reader==3.2.3',
        'parse==1.15.0',
        'qgrid==1.3.1',
        'opencv-python'
    ],
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/DanielScottEaton/TrenchRipper",
    python_requires='>=3.7',
)


#     - aiohttp==3.6.2
#     - async-timeout==3.0.1
#     - attrs==19.3.0
#     - backcall==0.1.0
#     - bleach==3.1.4
#     - bokeh==1.4.0
#     - click==7.1.1
#     - cloudpickle==1.3.0
#     - cycler==0.10.0
#     - dask==2.12.0
#     - dask-jobqueue==0.7.0
#     - dask-labextension==2.0.1
#     - decorator==4.4.2
#     - defusedxml==0.6.0
#     - distributed==2.12.0
#     - entrypoints==0.3
#     - fastparquet==0.3.3
#     - fsspec==0.7.3
#     - future==0.18.2
#     - h5py==2.10.0
#     - h5py-cache==1.0
#     - heapdict==1.0.1
#     - imagecodecs==2020.2.18
#     - imageio==2.8.0
#     - importlib-metadata==1.6.0
#     - ipykernel==5.2.1
#     - ipython==7.13.0
#     - ipython-genutils==0.2.0
#     - ipywidgets==7.5.1
#     - jedi==0.17.0
#     - jinja2==2.11.2
#     - joblib==0.14.1
#     - json5==0.9.4
#     - jsonschema==3.2.0
#     - jupyter-client==6.1.3
#     - jupyter-core==4.6.3
#     - jupyter-server-proxy==1.3.2
#     - jupyterlab==2.0.1
#     - jupyterlab-server==1.0.7
#     - kiwisolver==1.2.0
#     - llvmlite==0.32.0
#     - locket==0.2.0
#     - markupsafe==1.1.1
#     - matplotlib==3.2.1
#     - mistune==0.8.4
#     - msgpack==1.0.0
#     - multidict==4.7.5
#     - nbconvert==5.6.1
#     - nbformat==5.0.6
#     - nd2reader==3.2.3
#     - networkx==2.4
#     - notebook==6.0.3
#     - numba==0.49.0
#     - numexpr==2.7.1
#     - numpy==1.18.3
#     - opencv-python==4.2.0.34
#     - packaging==20.3
#     - pandas==1.0.3
#     - pandocfilters==1.4.2
#     - parse==1.15.0
#     - parso==0.7.0
#     - partd==1.1.0
#     - pexpect==4.8.0
#     - pickleshare==0.7.5
#     - pillow==7.1.2
#     - pims==0.4.1
#     - prometheus-client==0.7.1
#     - prompt-toolkit==3.0.5
#     - psutil==5.7.0
#     - ptyprocess==0.6.0
#     - pulp==2.1
#     - pygments==2.6.1
#     - pyparsing==2.4.7
#     - pyrsistent==0.16.0
#     - python-dateutil==2.8.1
#     - pytz==2019.3
#     - pywavelets==1.1.1
#     - pyyaml==5.3.1
#     - pyzmq==19.0.0
#     - qgrid==1.3.1
#     - scikit-image==0.16.2
#     - scikit-learn==0.22.2.post1
#     - scipy==1.4.1
#     - seaborn==0.10.0
#     - send2trash==1.5.0
#     - simpervisor==0.3
#     - slicerator==1.0.0
#     - sortedcontainers==2.1.0
#     - tables==3.6.1
#     - tblib==1.6.0
#     - terminado==0.8.3
#     - testpath==0.4.4
#     - thrift==0.13.0
#     - tifffile==2020.2.16
#     - toolz==0.10.0
#     - torch==1.5.0
#     - torchvision==0.6.0
#     - tornado==6.0.4
#     - traitlets==4.3.3
#     - trenchripper==0.0.5
#     - wcwidth==0.1.9
#     - webencodings==0.5.1
#     - widgetsnbextension==3.5.1
#     - xmltodict==0.12.0
#     - yarl==1.4.2
#     - zict==2.0.0
#     - zipp==3.1.0