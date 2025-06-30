Title: Moving from SaaS to metered billing
Date: 2018-06-12 22:19
Slug: moving-from-saas-to-metered-billing
Category: Business
Tags: saas, pricing, toofr, business-strategy
Summary: The scary but necessary transition of Toofr from traditional SaaS pricing tiers to a $9/month + metered billing model, prioritizing fairness over MRR.

I thought a lot about it. I even dreamt about it. Deep in my gut I knew the change would need to happen but I wasn't sure how or when. The thought would come and go and for the most part I ignored it.

Then one fateful day about a month ago I was in my Stripe dashboard and noticed an alert saying I was on an older version of the API. I knew I hadn't updated anything in my billing code for a while so since I had a few minutes I clicked in and looked at the changelog.

And then I found this: (https://stripe.com/docs/billing/subscriptions/metered-billing). Ho-ly-shit. That nagging sensation crept up and swept over me. This was it. This was how (https://www.toofr.com/), my email finding service, needed to bill. Not the tired old (https://kopywritingkourse.com/the-three-pronged-pricing-technique/), each with its own credit allotment and contrived gated features. I'd fallen into that trap, grudgingly, and was afraid to move out of it because hey, it worked. I was padding my pockets with it but the churn rate was high, at around 3X higher than I say it should be (https://www.amazon.com/Parallel-Entrepreneur-start-businesses-keeping-ebook/dp/B07CG8SV5V/).

How's that for irony? I couldn't even get my own company to look like the ideal side business I wrote about. My explanation was severalfold:

- I was comfortable. Making $15-20K on a side business is no small feat. I felt hesitant to rock the boat and potentially make a disastrous change.- I didn't want to build my own metered billing system. That's why the Stripe find was so critical.- My churn was high but my new revenue offset it. As a result, my growth was stagnant and choppy at best. Good months were offset by bad ones.

The result was stasis. I was frozen by fear: fear that a change to metered billing would ultimately make my revenue irreversibly worse and fear that I would also waste a bunch of time in the transition.

One thing I learned from past startup experience is operating from fear is a terrible way to run a business. It may not lead to disaster right away but it's the inevitable result. I was repeating a known mistake. I knew it, but I wasn't doing anything about it.

---

About a month ago, after consulting with a few startup founders and pondering the change on Twitter, I started offering my first metered billing plan at $29/mo. It included 2,900 credits (a penny each) and additional credits would also run a penny (a credit gets you an email address, verification, or other unit of usage on Toofr).

I sold subscriptions! Sometimes four in a day. That felt good. I was onto something. The change was working. I didn't need to manage the existing customers because I designed the metered billing system to work with legacy plans. They'd simply move to metered billing when they ran out of credits. It was clean and simple.

However, although this was better, I still wasn't 100% happy with the change. It felt like I was only flirting with metered billing by essentially forcing everyone onto a single SaaS-like plan. What if someone only wanted to use 100 credits? I was still making them buy 2,900 every month.

It crossed my mind that maybe the plan shouldn't come with credits. It should be like a membership fee you pay to get *access* to the tooling and the *usage *of the tools would be billed separately. I also read some posts and listened to some podcasts that re-iterated that higher paying customers are way better than lower paying ones. At essentially $29/mo I was playing solidly in the bottom tier.

So about two weeks ago I put up a $99/mo plan that had no credits and let it sit. I sold exactly zero. Nada.

Then two days ago I adjusted that price down to $9/mo, also with no included credits, and sold six. So far today I sold another four.

Then, just a few hours ago, I took a deep breath and made the scariest change I've ever made. I essentially wiped $10,000 off of my MRR by moving all of my high-paying customers, everyone on my old $49/mo, $99/mo, and $249/mo plans, down to the $9/mo plan. I didn't ask. I just did it.

It sounds crazy to proactively move customers from high monthly plans down to essentially nothing. I've never done it before and I've never heard of anyone else doing it. Yet here I was, one by one, lowering my MRR by hundreds of dollars per customer.

Then it was done. Here's the email I just sent to my customers:

*Hi all,*

*I’m bcc’ing everyone who is now on a $9/mo Toofr plan. Some of you signed up for it, some of you just got moved over to it, and others were on a slightly more expensive iteration of it. Regardless, it’s all one big Toofr plan family now. So what’s the deal? *

*Briefly:*

- *Toofr is not really a SaaS product and it didn’t feel right to pretend to be one. Toofr should be charged based on actual usage, so that’s what I’ve done. Welcome to metered billing!*- *$9/mo is not a lot of money. My “MRR” is definitely going down after this, but I hope to make it back with better retention. The purpose of the monthly charge is to make sure your credit cards are still working, not to make money :)*- *If you moved from another plan that had credits, you get to keep your credits! When you use them up, you’ll automatically be on metered billing from then onwards.*- *If you already had 0 credits, you can start using Toofr in metered billing mode immediately.*- *Remember, you’ll still get invoiced and charged once a month and that invoice will combine the $9/mo part with the metered billing part. If you don’t use any credits, it’ll just be $9. If you use credits, you’ll be billed $9 + $0.01 per credit. Simple!*

*You can also now see your usage history at https://www.toofr.com/pings and your balance is always visible in the top right of the Toofr nav. *

*Got questions? You got my email :)*

*Ryan*

---

It's some scary shit, especially for a guy who is depending on Toofr to pay my half of the mortgage, car, and childcare bills. I did do some database digging to see what the metered billing charges should look like going forward and it offset the loss enough for me to pull the trigger on the change. My MRR is definitely going to drop but I do expect retention to be better.

The money I'm primarily going to lose is from those who signed up for a $49+/mo dollar plan and stopped using it months ago. I'll only get $9/mo from them now. On the one hand that's a bummer but on the other hand it's more fair. When they do come back there should be less frustration, less angst, less regret, less submission to the idea that I got them, I won a few rounds against them. These are my customers, after all. Not my adversaries.

Toofr now stands out among my email finding peers as the only company without a traditional SaaS model. I'm equal parts proud and scared, but it's a good type of scared, the aware-and-in-control scared as opposed to the fear-of-my-own-shadow scared.

I might come to regret this but I'm optimistic that I'll ultimately be rewarded for treating my customers better, being on their team, and treating them the way I'd want to be treated.

I'm hoping that the golden rule brings home the gold.