# easy_torch_install
It can help you quickly complete the installation of a matching torch version with cuda.
## Why I create this repo?
I've often struggled with mismatches between torch versions and CUDA versions. If you're facing the same issue, you might want to try my script.
## How to use ?
```
conda activate your_env
python fast_install_torch.py
```
## How it work?
When you run this script, it will automatically detect your CUDA version, run on **the current cuda environment(change the cuda env manually please)**, and select the torch version you want. It will then automatically complete the download. There's no visual progress bar during the download process, so please be patient and wait for a few minutes. You'll be notified when the installation is complete. 
(Note: If the CUDA version can't be matched, it's recommended to choose a version higher than your current one. For example, if I have cu115, I would select cu121, and then choose the torch version I want.)

