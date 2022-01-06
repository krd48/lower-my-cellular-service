# Reddit api to advertise for a MVNO (mobile virtual network operator)

* I really enjoy keeping the money. I'm not cheap, but I am frugal. Going from a few years back, signing up for the verizon unlimted plan ran $85-90 a month, with a $40 activation fee, or even going prepaid with AT&T still set me back $60/month, when most of the time I had WIFI access.

* Recently, I discovered the world of MVNO's. It's basically excess bandwidth major carriers sell off that isn't used. The one factor is speeds are depritorized during times of internet traffic - your webpage may load a few seconds slower at 5pm in a crowded city then everyone elses website.

* I discovered the MVNO, visible, who uses verizon towers. It started at $40/month, unlimited everything, including hotspot. If you joined a party of 4 people, you could pay $25/month (there way of keeping people using there service).

* They even had a way to get your monthly service to $5/month, by basically advertising the service. Natuarally, there was a subreddit where people spammed referral codes when they had a chance. For everyone person who joined using your visible referral code, you both got the 1 month of $5 cell service, up to 12 months at any given time you can cache.

* I started posting ad's on the subreddit for people to join using my code, and quickly my post went down the subreddit as posts came in. I got a few referrals, but it tooks days to get just 1 person to see my code and too much time. 

* I decided to use reddit's api and windows task scheduler to simply post to the subreddiy my referral code link on a few different schedules after watching post times the few weeks I was trying.

* Pretty simple task, but now my cell service will cost $60 for atleast the next year at $5/month, whereas, with AT&T prepaid, I was paying $60/month. So my cost savings the next year will atleast be $660, but probably more since I can only hold 12 referral credits at any given time. When I pay my next bill, I will lose 1, then can refere someone else to gain one more credit, to be back up to 12 credits, or 12 months of service at $5 each.

* And honestly, the service has been great so far. I can't even tell a difference from when I was paying $90 at verizon for I think it was the get unlimited plan.

* Used reddits api and library PRAW to interact with the API (good library with lots of functionality, can comment on posts, upvote/downvote, etc.) and windows task scheduler.
