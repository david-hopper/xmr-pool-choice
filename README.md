# xmr-pool-choice
Choose the best Monero mining pool, while maintaining the core values of the network.

Summary:
This collection of python scripts currently scans the currently accepted Monero
mining pools and runs some diagnostics on them to determine the optimal case for what you should be using.

The best pool is determined by taking into account a few quantities that are important for both the miner as well
as the Monero network as a whole. First and foremost, decentralization is favored, thus pools with lower hash rates are favored. 
Second in importance is the ping time, as I have found lower ping times lead to better stabilitity and longetivity of a miner staying connected. These two criteria are the first to be implemented, but I intend to add functionality for measuring the normalized variance in the pool hash rate (with the idea of avoiding pool hoppers) as well as analyzing the luck factor of the last N blocks. However, these will require some more work I haven't fully thought out.

Usage:

