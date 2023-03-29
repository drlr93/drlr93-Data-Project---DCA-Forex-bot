# drlr93-Data-Project---DCA-Forex-bot
drlr93/Data-Project---DCA-Forex-bot

In the following project, we create a DCA bot that can invest in the forex market based on the direction of the currency pairs.
Management risk is controlled using the dollar cost averaging technique.

To predict the direction of the market, we select 3 uncorrelated currency pairs and find the market trend using 2 EMAs (8 and 5).

![image](https://user-images.githubusercontent.com/98351714/225906878-f70ab4f8-f6e9-4151-9374-38792cba647c.png)

We can see the result of the simulation process.

![image](https://user-images.githubusercontent.com/98351714/225905033-080e46ac-10c6-4301-a9a0-da8219c988f5.png)

If the market goes in the opposite direction, the bot opens a new market order with higher volume than the previous orders to promediate.
Position closing is done by the bot on the profit target by symbol or manually to cut losses.

![image](https://user-images.githubusercontent.com/98351714/225906707-99b4b51e-1bd7-45ff-8154-2578e39df5bf.png)

Financial report indicates good trading performance.
