# Set of tutorials
1. Super Cloud @ MIT Tutorial - How to run code on a supercomputer in parallel.
2. mpyfit tutorial - How to fit any dataset using mpyfit (instead of scipy.optimize.curve_fit, which does not allow as much customization)


# 1. Super Cloud @ MIT Tutorial
 
1. Download the tutorial code from github onto your computer: https://github.com/zdebeurs/Tutorials
2. Open the jupyter notebook by typing the following in your terminal: <p><code> jupyter notebook SimpleParallelScript.ipynb </code></p> 
3. Read through the comments and see if you can run the script.
4. Next, let us run this same script on the supercloud instead. 
5. Log into the supercloud using your terminal:  <p><code> ssh USERNAME@txe1-login.mit.edu </code></p> 
6. Open another terminal window and copy the directory to your SuperCloud directory: <p><code> scp -r filepath/Tutorials USERNAME@txe1-login.mit.edu:/home/gridsan/USERNAME/Tutorial_Supercloud </code></p> 
8. Let us see how we can submit our script to the supercomputer. Type <p><code> cat slurm_scheduler</code></p> 
9. Now let us submit this job by typing
	<p><code> sbatch slurm_scheduler</code></p> 
10. Check the status of your job by typing <p><code> LLstat</code></p> 
11. If the job is done (likely not listed with LLstat), type <p><code> ls</code></p> 
12. You should see an output file that looks something like this: <p><code> Tutorials.sh.log-11540612-4294967294</code></p> 
13. To read its contents, type <p><code> cat Tutorials.sh.log-11540612-4294967294</code></p> 
14. And you’re done! 


# 2. mpyfit tutorial
1. Download the tutorial code from github onto your computer: https://github.com/zdebeurs/Tutorials/mpfit_tutoral.ipynb
2. Follow the instructions in the jupyter notebook and run the cells.

