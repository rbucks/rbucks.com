Title: Toofr LLC quarterly report: Q2 2018
Date: 2018-07-31 22:22
Slug: toofr-llc-quarterly-report-q2-2018
Category: Business
Tags: toofr, entrepreneurship, business-strategy, saas
Summary: Q2 2018 quarterly report on switching Toofr from SaaS to metered billing - a risky move that dramatically improved all key metrics and customer growth.

I write this from the creek in my backyard where the mosquitos are celebrating this oddly cool summer morning in Walnut Creek by devouring my shins. I like to work down here anyway. It's a reminder that nothing is perfect and it'll also force me to type a bit faster.

Q2 ended with a really huge change: [moving from SaaS to metered billing]({filename}moving-from-saas-to-metered-billing.md). It was scary as shit. It could have tanked my business. If I had investors I might not have gone through with it. In fact, if I had a team beyond myself that relied upon this income, I might not have done it. I would have convinced myself to "leave well enough alone." That would have been the wrong move, though. This change has worked wonders for my business. Every metric I care about shot upward in the 45 days since I made this change. I have no regrets.

This report will cement my case for metered billing. Like working from a creek, it too is not perfect. There are bugs, but also like working from a creek, I'd take this over the traditional alternative.

### The case for metered billing

Toofr is not a software product. There's a user interface my customers log into, but it's not software the way that Salesforce is software. The utility in Toofr is not to stay logged in, using it for most of your day. No, you log in, use it, and get out and prospect. That's what it's built for, and frankly, that's why I haven't invested in some beautiful UI/UX. I don't care and neither do my best customers.

So why did I bill the way Salesforce bills? Why did I put SaaS-like pricing plans on Toofr, making up a features to gate that arguably added no real value to my customers? I'll explain by breaking this down a bit further.

The following pricing chart from Toofr a few months ago should look annoyingly familiar.

!(https://media.licdn.com/dms/image/C5612AQEgou6Kk1ubuQ/article-inline_image-shrink_1000_1488/0?e=1554336000&v=beta&t=BuUh06gpsBvczRHLiCCWuZptpyjfbIBtRGoGzaWMJnY)

There are bunch of problems with this pricing, but it got me to about $15K/mo in revenue and $10K/mo in profit even while it was merely a side project. As Toofr grew, and as I had more time to put into it, I kept running up against this central problem:

My biggest customers were barely profitable and they were making Toofr worse for everyone else. This is not how it should be! Salesforce's biggest customers are surely their best and most profitable. What was I doing wrong?

The problem is my COGS are metered but I was billing as SaaS. I don't get any pricing breaks from Heroku or Google or any of the other third parties I use. And yet, in this traditional SaaS pricing scheme, I'm giving steep pricing breaks that bring my margin within a hair of zero. In fact, I ran the numbers and saw that Toofr's lowest tiered customers were subsidizing its highest tiered customers.

That's completely "bass ackwards" as my high school-aged self would say. I should be making more profit on my big API customers, not less. This pricing was screwed up.

At the same time, my churn was high. You can see here in the months leading up to the switch to metered (I did that in mid June) my revenue churn was consistently over 10% and north of 20% on a bad month.

!(https://media.licdn.com/dms/image/C5612AQHJA7eB-B6aBg/article-inline_image-shrink_1500_2232/0?e=1554336000&v=beta&t=q6sS_FCJHMAfOuXZeKtt6CxPPN7daePgMHXO6wRtQzc)

Now you can see in the header banner that it's since dropped to 1.3%. I went from 12% churn to 1.3% churn in just one month. That's insane! To make sure these numbers are accurate (I did switch from ProfitWell to Baremetrics for my subscription analytics during this time) let's also look at the user churn. They should have a similar movement.

As I've written before, one of the numbers I care most about, because I believe it will add the most value to Toofr when I sell it, is the number of active customers. I'd been very disheartened by the drop in active customers in the beginning of Q2. Here's the ProfitWell chart on that drop.

!(https://media.licdn.com/dms/image/C5612AQHhSBcISfSuqg/article-inline_image-shrink_1500_2232/0?e=1554336000&v=beta&t=nVYUzM6tRqOQCtxR4DBZmWvReoeu6FE24fTkhN0Hh08)

I'd been acquiring fewer and churning more, resulting in a net drop in customers in some months. Overall it was a very slow climb, and slow growth at a small company like Toofr is a bad, bad sign. This played a role in my decision to toss convention ((https://www.businessinsider.com/marc-andreessen-advice-to-startups-raise-prices-2016-6) (https://www.inc.com/jim-schleckser/why-you-need-to-raise-your-prices-today.html)) aside and *lower *my prices and get off the SaaS train altogether.

Here's what happened to my customers (Baremetrics table now).

!(https://media.licdn.com/dms/image/C5612AQH9xRuSVYu3GA/article-inline_image-shrink_1500_2232/0?e=1554336000&v=beta&t=GioO6aEfUQMUvxIfs0R-VUX-tGAHcI5p2I4c4mYaRuk)

We're up! In fact, 259 is the most active customers I've ever had. I've written that 300 is the magic number. If I can get 300 active customers then I can sell Toofr for $1M. I'll have to wait to prove this out, but I'm optimistic. I should be there next month.

!(https://media.licdn.com/dms/image/C5612AQGExtBy1jZCfg/article-inline_image-shrink_1500_2232/0?e=1554336000&v=beta&t=ESkfuxDm7Iv_8tybPXcrtwpEPRUra6sHnSIy8QfgFtk)

Interestingly, around February 2017, the bottom of that dip in customers, is when I left Scripted to go full-time onto Toofr. Toofr was making money in that long customer decline between June 2015 and February 2017 but it was beginning to atrophy. Active customers are the lifeblood of any business and Toofr was losing them hand over foot while I was (https://medium.com/@rbucks/whats-next-for-me-a6418447d3d0), (https://themighty.com/2018/01/my-papillary-thyroid-cancer-story/), and welcoming my second daughter.

You can see things have improved a lot since then. Phew!

But zooming in on Q2 of this year, as I showed in earlier tables, presented a less bright picture. I still had churn issues, revenue was flat if not down, and Toofr was not looking like a healthy business to buy. My dreams of a 7 figure exit were not looking so great.

So that's the stage for June 12, 2018, when I made the big change. I (https://www.linkedin.com/post/edit/moving-from-saas-metered-billing-ryan-buckley) immediately after I did it. I wanted to celebrate and type away my anxiety. Now, a month and a half later, I have some more perspective.

### Why metered billing works

Metered billing works if you are providing a discrete data product. It turns out this is all I do. I don't like building software but I do like building data products. Here are the pricing pages for (https://www.inlistio.com/) and (https://www.enps.co/), my two other data products.

Yea, I'm pretty much tripling down on metered billing now. One plan for all customers, large and small. Here are three reasons why I'm all in.

### No new plans

(https://media.licdn.com/dms/image/C5612AQFpiod9S2eF9Q/article-inline_image-shrink_1500_2232/0?e=1554336000&v=beta&t=SPQ_Wz2AILCuGwcmyPMGH4ouCRaWz0o2NunM8pMOnDM)](http://www.google.com/url?sa=i&source=images&cd=&cad=rja&uact=8&ved=2ahUKEwjYq_Op_cncAhWFAXwKHZogB9oQjRx6BAgBEAU&url=https%3A%2F%2Flumelle.wordpress.com%2F2014%2F06%2F13%2Fthe-no-new-friends-phenomenon%2F&psig=AOvVaw241gjqWq5T6u5MWEAhk5Wn&ust=1533148475115407)

If I want to change the price of the meter, I can do that without worrying about grandfathering old customers. I don't have to manage tons of legacy plans. I can simply change the meter.

At its peak, Toofr had 40 different Stripe plans. That's ridiculous. It should be easier to experiment with pricing than that, and yet I'm sure I'm not alone. The main thing I changed with those pricing plans was the effective cost of a query.

My competitors charge anywhere from 10 cents down to a fraction of a cent for an email address. Now I charge just $9/mo and a penny per email address. I don't think I'll ever make a new plan for Toofr again. The $9 produces some revenue and that will grow over time (especially if the current customer growth rate continues) but that $9 charge has the other benefit of making sure the credit card works so a rogue customer can't rack up a bunch of metered charges on an old busted credit card.

Here's the Toofr plan to rule all plans. My largest customer now spends about $10K/mo. My smallest one spends $9. They both pay the same $0.01 per email address. It's a simple, elegant solution to what was a complicate pain in the neck.

!(https://media.licdn.com/dms/image/C5612AQG3C6kkWtAWKw/article-inline_image-shrink_1500_2232/0?e=1554336000&v=beta&t=YXdKl7HYDBH9IjSUOTnfHfcdRHnVuzlBtaJQKZ6WNpA)

### Superfluous gating is lame

Making up excuses to charge more to your customers is... lame. I know why it's so common. Until a month ago, I did it too. The thing is, customers are smarter now. They know what actually costs you money to provide and I think they resent it (as I do now) when there's a price hike for something that doesn't actually cost them any extra money to provide.

The counter argument here is that companies should charge based on value. It doesn't matter what it costs, they'd argue. It matters what the customer is willing to pay.

That's fine for pure software, but when your product is data, it really doesn't make sense to gate software features.

I like how (https://www.pipl.com/) does their (https://pipl.com/api/pricing) (even though I wish it were a lot lower). This makes sense to me. They essentially gate on the kind of data they provide but it's a pure metered billing system.

!(https://media.licdn.com/dms/image/C5612AQEEufFchxqwfQ/article-inline_image-shrink_1500_2232/0?e=1554336000&v=beta&t=8sqWpH4SWxY8pYAdk68deberKAslryRuQ0EzJvCuEgA)

You can upgrade to premium coverage and those per match prices go up 2X. It's brilliant, really, and I think I'll take a page from this book sometime next year and charge different metered rates on Toofr products.

Let's compare this to (https://www.fullcontact.com/). I think (https://www.fullcontact.com/pricing-plans/) is lame. It's why I don't use FullContact anymore. First of all, the plan without pricing is not the most requested. They need to stop trying to be cute. Secondly, going from $0 to $499 is a huge jump. Why can't they be metered just like Pipl? It's basically the same data, the same product, the same customers, with two completely opposite pricing schemes.

FullContact should focus on giving their entry level customers a great experience and allowing them to grow into greater spend by **simply charging for what they consume**. If FullContact had a metered plan I would still be using them. Because they don't, I've switched. I don't miss them.

!(https://media.licdn.com/dms/image/C5612AQFwnzhpAlVZEA/article-inline_image-shrink_1500_2232/0?e=1554336000&v=beta&t=gxRRNTp1MYcEuv-klmLs6wc3l8h6I38tCQZaaB_7i7A)

Unlike FullContact, Baremetrics is a software product. They provide subscription analytics. I log into it, noodle around, maybe grab a chart or a little bit of data, but the product they provide is software that analyzes my customer data. Since I can't really control how much data goes into Baremetrics (Stripe feeds it to them automatically), it wouldn't make sense to charge me in a metered manner.

And since (https://twitter.com/Shpigford), their CEO, is a pretty thoughtful guy, I figured they'd have a thoughtful approach to pricing. Indeed they do.

!(https://media.licdn.com/dms/image/C5612AQHkLloKWom3XQ/article-inline_image-shrink_1500_2232/0?e=1554336000&v=beta&t=lxaao3PkIn354MLCgIXmut5tCleLUZ_ddz4TMvyjoqg)

They price on value and they tie it to how much money your company is generating. I'm in that $100/mo tier right now and the interesting thing is Baremetrics probably spends more on computing and storage for my account because of my low price point and higher number of customers than the typical customer in this bucket. The higher the ARPU, the fewer customers will fit onto this plan. Less customer data is less headache and cost for Baremetrics.

Yet they don't tier on customers. They tier on revenue, figuring that the more revenue I make, the more I'm willing to spend on analytics because the stakes are higher and I'm probably checking it more often.

It turns out Josh and his team are correct. This pricing makes sense to me. It's priced like SaaS because it is SaaS and they found a clever way to increase price with value added.

That's the difference.

### Faster sales cycles

Shortly after the pricing charge I got two new large customers for Toofr and another big one for Inlistio. Combined they spent about $6K in just a few weeks. The common thread across these guys are they worked for real, legit companies and **they never contacted me** before spending $1K+ on my products.

I think there's something about a low monthly "membership" and metered charges in the pennies per unit that feels safe. You can put your credit card down, try it out, and then go all in. They like not having to contact me. I have my email and phone number everywhere but not a single one from this group reached out to me. I had $1K/mo+ Toofr plans and I had a no-contact sale only once. It usually doesn't happen with SaaS pricing but it's looking good so far with metered.

I am definitely having fewer conversations about pricing. It's rare for someone to come in with questions. I think they're willing to bet $9/mo that Toofr will solve their problem. It's not risky.

Interestingly, in this move to metered I also removed the automatic free trial. The signup process before looked like this:

- Registration -> Email confirmation -> Automatic 12 free credits -> Prompt for subscription when credits are low

I had a bunch of people signing up over and over again with fake email addresses. I had one guy who did the jeremy+1, jeremy+2, jeremy+3, etc, all the way up to jeremy+40 so he could use a few hundred free credits. (https://blog.hunter.io/99-of-our-users-are-not-paying-and-its-perfectly-fine-f7011439fa52) and are happy that only 1% of their users are paying. I'm happy for them -- so I refer people who don't want to pay for Toofr their way. I got tired of these customers who would probably never pay. The new funnel looks like this:

- Registration -> Prompt for subscription

I don't bother confirming emails because it doesn't do someone any good to register a bunch of times. If they click off the subscription prompt, they see one of these blocks. Good ol' Blue Boy is now my top sales rep.

!(https://media.licdn.com/dms/image/C5612AQFmiWf5Bmv-Bw/article-inline_image-shrink_1500_2232/0?e=1554336000&v=beta&t=HrzsRFu9oiuRB1hYis2nvBGmBL48QquFTh0D0lzcNfs)

If someone really wants some free credits, they'll write in and I'll give them credits. I'm formalizing this trial process now so I can get visibility into the conversion rate. If it's too low then I'll stop giving away credits. Hunter can have those guys.

Metered billing, with the low entry payment, has given me the confidence to put up a stricter pay wall. I don't feel bad about asking people to pay $9/mo to try it out. And as you can see in the active customer numbers, it's working.

### Granularity is king

Straight lines are better than steps. I'd rather let customers pay just for what they consume.

More customers are better than fewer customers. I'd rather have five $9/mo customers than one $49/mo customer.

A company ultimately is like an ecosystem. The more life it has, the healthier it is and the longer it will last. It can withstand stress better and it will grow faster. That's the game I'm playing now and it feels right.

I'm treating my customers the way I want to be treated. I'm billing my customers the way I want to billed.

There has to be sustainability in that.

### Hey, show me the money

Oh, money? Right. It's choppy but should smooth out in the coming months. In the meantime there's enough to pay the mortgage.

!(https://media.licdn.com/dms/image/C5612AQFLD8KWlFWlSw/article-inline_image-shrink_1500_2232/0?e=1554336000&v=beta&t=kV_XOc7-WgcFeRJ4Hc0-CmB7rFxDb8pOsg1ZHSnmBhM)