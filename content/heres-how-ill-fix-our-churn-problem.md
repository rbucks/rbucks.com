Title: Here’s how I'll fix our churn problem
Date: 2017-01-05 16:39
Slug: heres-how-ill-fix-our-churn-problem
Category: Business
Tags: churn, SaaS, business strategy, data analysis

The biggest problem we have at (https://www.scripted.com) is churn. The second biggest problem, and it’s related, is burn.

Sounds funny, churn and burn, but together they can make or break your business.

We measure churn as the number of cancellations this month divided by the number of active subscribers at the end of last month.

![Churn formula diagram]({static}/images/2dd3f-13cfltfrr-kbhq-ly3iubka.jpeg)

Without putting something out on the internet that I’ll regret later, I’ll just say ours is above 10%. It should be below 10%. It needs to be below 10%. To get it below 10%, we need fewer subscribers to cancel (the numerator, above). To do that, we need to do… something. Figuring out what that *something *is has been a major challenge. Here’s a study on it.

---

Churn is a difficult problem to solve because it’s multifaceted. If you’re operating your business thoughtfully, then there won’t be a single reason for high churn. If you’re claiming to sell hotdogs and you’re sending people bananas, well, there you go. Sending hotdogs will fix your bad churn problem, but it may not get it into *good *territory.

> A good churn is under 5%. That’s 5% per month if you’re selling monthly subscriptions and 5% per year if you’re selling annual contracts.

Some churn happens because businesses go out of business. Other times the champion, the main user of your product, quits, and your deal goes out the door with them. And, of course, sometimes you lose the customer because your app messed up or didn’t meet expectations.

Sometimes churn is your own darn fault. You sold them a hotdog and promised a banana. But not always, and when it comes to churn, the obvious problem is never the only problem.

### **Figuring out when to contact trials**

Here’s where I struggle.

Scripted is a pretty small team. Today we’re just 15 full-time employees (our thousands of writers are contractors). With over a hundred new companies starting trials every month, and over 500 active subscribers now, we can’t reach out to every single one manually as their subscription renews. And I certainly can’t do it every month.

Besides, how annoying would this be?

> Hey Mrs. So-and-So,
> 
> It’s just me again. I emailed you last month around this time too. How’s your Scripted membership going? You’re not gonna cancel on us, right?
> 
> Lol.
> 
> I saw you got a couple of blog posts from us last month. Joe’s a great, isn’t he? He’s one of our newest top writers.
> 
> …But really, you’re not cancelling..?
> 
> Cool beans. C ya next month!
> 
> Ryan
CEO :)

Even if this was a good idea, I simply don’t have the bandwidth to do it every month. So how do I choose who to contact? Which criteria do I use? How do I know who’s about to churn? And of those, how do I prioritize so I spend my precious time on the best customers?

Here’s where a histogram can help.

![Trial cancellation histogram]({static}/images/95eda-1fhxkvwpwzxbhbks3-pwujg.png)

Scripted offers everyone a 30-day free trial, so the trial cancellations show above in the first four bars. These guys never paid for a membership; they took the free trial and bounced.

Of note are the people who cancelled within the first 7 days. They probably didn’t even get a writing job back before they cancelled. It’s likely that they had no intention of staying beyond the free trial, either because they had a one-time need or they meant to sign up as a writer instead of a business. Who knows? Regardless, I don’t (have time to) care about these people.

The other clear spikes are the week before and the week after the trial conversion (around day 30). This is when they first pay us, and we send out some warning emails that effectively say, “Heads up, your trial is wrapping up and we’re going to charge you soon…” We implemented this to reduce the number of chargebacks and complaints. Our complaint problem went away, but our churn problem got worse.

Here’s my takeaway.

![Conversion window diagram]({static}/images/59d90-19fjlmsf8v2ecvnzn4888za.png)

I have a window of a couple of weeks to save the people who don’t cancel in the first week.

Again, I’ll just let the first week cancelations go. If they don’t even try us, then they’re not real customers and were probably misinformed when they started a trial, or never intended to convert. The guys who cancel in the latter half of the month are the ones I need to save, so I’ll focus my interventions on people whose trials started more than a week ago and haven’t canceled.

That’s a pretty actionable takeaway.

### Figuring out when to contact converted customers

I bucket the churn problem in two categories: trials and customers. The approach should be different for people who are active and people who are just starting out.

If we get a bit more granular and look at what point *in the monthly subscription cycle *they cancel, we see a pretty even distribution.

![Monthly subscription cycle histogram]({static}/images/70720-1pedkv72xvn4gjlag0547nq.png)

Unfortunately there’s not a lot to play with here. Clearly there’s an “Oh shit” group in the 0 to 7 bucket that cancels as soon as the renewal gets charged. Otherwise, it looks like if someone wants to cancel, they’ll do it at whatever point in the month the decision is made. So I can’t really use the renewal cycle to prioritize churn.

In fact, the answer here requires a different data set. Account activity (or lack there of, really) is a pretty good predictor of churn. Guess what? Here’s another histogram!

![Account activity histogram]({static}/images/0249b-1rzggxogd1eyyoduygdfqoa.png)

The -1 here means they never ordered a job. So here’s a an easy takeaway:

**Reach out to people who subscribe and never order a job!**

The next big spike is in the second two weeks after their last order. This one is nuanced though. We have a lot of happy customers who only order one or two jobs a month, and I don’t want to annoy them with an unnecessary check-in email.

Instead, I’ll focus on the really long tail after that first month. To give a sense of the relative sizes here, for every 10 people who cancel without ever ordering a job, there are 30 who cancel within a month of ordering a job, and another 30 who cancel some time after that. My takeaway is this:

**Reach out to people who haven’t ordered a job in 30 days!**

---

I think that’s enough analysis to keep me busy for the next few weeks. To summarize how I’m going to reduce our churn rate, here’s the summary, from the top.

- For new trials, I need to contact the people who didn’t cancel after the first week.- For converted trials, I need to contact the people who haven’t ordered a job within 30 days.

I’ll track who I’ve contacted and see if these hypotheses work out.