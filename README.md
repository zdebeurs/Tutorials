# Tutorial_Supercloud
 
1. Download the tutorial code from github onto your computer: https://github.com/zdebeurs/Tutorial_Supercloud
2. Open the jupyter notebook by typing the following in your terminal: <p><code> jupyter notebook SimpleParallelScript.ipynb </code></p> 
3. Read through the comments and see if you can run the script.
4. Next, let us run this same script on the supercloud instead. 
5. Log into the supercloud using your terminal:  <p><code> ssh USERNAME@txe1-login.mit.edu </code></p> 
6. Open another terminal window and copy the directory to your SuperCloud directory: <p><code> scp -r filepath/Tutorial_Supercloud USERNAME@txe1-login.mit.edu:/home/gridsan/USERNAME/Tutorial_Supercloud </code></p> 
8. Let us see how we can submit our script to the supercomputer. Type <p><code> cat slurm_scheduler</code></p> 
9. Now let us submit this job by typing
	<p><code> sbatch slurm_scheduler</code></p> 
10. Check the status of your job by typing <p><code> LLstat</code></p> 
11. If the job is done (likely not listed with LLstat), type <p><code> ls</code></p> 
12. You should see an output file that looks something like this: <p><code> Tutorial_SuperCloud.sh.log-11540612-4294967294</code></p> 
13. To read its contents, type <p><code> cat Tutorial_SuperCloud.sh.log-11540612-4294967294</code></p> 
14. And you’re done! 
