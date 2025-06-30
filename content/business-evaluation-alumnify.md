Title: Business evaluation: Alumnify
Date: 2022-12-29 21:03
Slug: business-evaluation-alumnify
Category: Business
Tags: business evaluation, b2b data, saas, marketing

I like B2B data businesses. I learned how to write web applications by building Toofr.com (now [FindEmails.com](https://www.findemails.com/) -- they kept my "oo" logo after I sold it). Toofr found email addresses for business contacts. I wrote a book, [The Parallel Entrepreneur](https://rbucks.com/the-parallel-entrepreneur/), about my experience building, running, and selling Toofr while I kept a day job as co-founder of [Scripted]({filename}the-scripted-origin-story-as-i-remember-it.md).

I took some time off after selling Scripted and built a few more B2B data companies. TrackJobChanges automated some clever Googling to figure out current employment status and alert when a business contact changed jobs. (https://www.emailfinder.io) did what Toofr did, but better, and in bulk. (https://www.name2domain.com) found the right website for a company name. TrackJobChanges made the most revenue and it utilized both EmailFinder and Name2Domain. In fact, Name2Domain powered EmailFinder's domain identification. If I entered "Bill Gates" at "Breakthrough Energy" into EmailFinder, Name2Domain would be called on to turn "Breakthrough Energy" into breakthroughenergy.org, and then the email finding trial and error would begin.

It was fun stuff, but it was a grind. After a few years at this, I decided to sell all three apps to (https://www.livedatatechnologies.com/). I was already friendly with the CEO and he invited me to continue working on a retainer to pump up their combined revenue. I ended up spending most of my time on EmailFinder, helping to shore up its resources. Live Data operated on a scale orders of magnitude larger than me. That was challenging work and it required all of my creativity. We made it happen though, and I learned how to use Heroku workers to scale a web app to previously unimaginable levels.

When my year was up after the acquisition, I re-focused my energy on MightySignal and [teaching at DVC]({filename}why-im-applying-to-be-an-instructor-at-dvc.md). That didn't last long; after a few months, I was back on with Live Data, this time to focus on TrackJobChanges (it now redirects to a similar but better Live Data app) and launch something we're calling Live Data Labs. I'm excited to share our progress!

The first app in the Live Data Labs portfolio is (https://www.alumnify.ai/). Alumnify taps into Live Data's trove of tens of millions of real-time B2B contacts. The idea is to focus on alumni of companies and schools. Why? I'll get to it.

Let's now evaluate Alumnify.

## The Problem

The problem, I suppose, for most B2B data companies is that LinkedIn won't share employment data. If LinkedIn opened up its API, a lot of B2B data companies would go out of business. I don't see this happening, though.

Here are the two sharpest pain points that Alumnify addresses:

- Nobody is tracking college and university alumni. Alumni associations can't access registrar records due to privacy constraints. They need to get a list of past and recent alumni to invite into the association, but it doesn't exist.

- College and company alumni both make great marketing segments, but LinkedIn doesn't provide a way to download a comprehensive and accurate list.

The two problems are distinct. The first, felt primarily by alumni association directors, is truly core to the job. Figuring out who is an alum of a college or university is a painstaking process. I know this first-hand as a board member on the DVC Foundation. We're creating a new alumni association and the data is sparse. Alumnify would help a lot!

The second is a problem that every online marketer will know. There's always a need for more data, more targeting, more lists. Sending marketing material to every Harvard or UT Austin alum is a compelling offer. There's no way to do this now. Recruiters feel this pain too. If they want to recruit from Goldman Sachs or Stanford, they can do it manually on LinkedIn, but they can't scale that effort up.

How big is this problem? I don't know. It could be huge. It might be small. It's not nothing, though. It feels to me like this is a big enough problem to put some effort into solving.

## The Solution

Alumnify is already live: (https://www.alumnify.ai). It takes a company name or school name and provides summary information about the alumni of that institution. It gives a sense of where they are and what they're doing. For a fee, it allows a marketer to purchase a list of everyone who worked at the company or went to the school.

The technology behind it is crazy. I still don't know exactly how Live Data does it, but they've found a way to combine multiple data sources to produce an accurate profile of employment and education history on 70 million people. I've been assisting in identifying emails for all of them and thinking up more compelling ways to present this information.

So that part of the solution is technical. The rest is a marketing challenge: how do we package this data and make it accessible? This is what we're in the midst of figuring out now.

## Customer Profiles

Alumnify needs a growth hack. There's one in here... somewhere. I have a few ideas, but let's break this down into who the ideal customer profiles for Alumnify.

### College Director of Alumni Relations

The head of alumni relations at a college or university is responsible for staying in touch with graduates. They usually are fundraisers, building relationships over time and developing an annual fund. To do this work well, they need an ever-growing list of alumni to contact. Since the registrar can't share this list, the alumni relations teams put a lot of effort into reaching students while they're on campus. Once the students leave campus, Alumnify will be the best tool to track their professional updates.

### Head of Digital Marketing

The head of digital marketing for a startup is responsible for finding more leads in an ever-competitive environment. Since past employment and education work as proxies for all sorts of things -- ambition, interest, geography, income -- alumni lists offer useful targeting. Alumnify will give names, current employment, LinkedIn profile ID, and an email address. This data should be sufficient for digital marketers to build lookalike models in Facebook or Google to further expand reach.

### Recruiter

This profile might be the most obvious. A recruiter at Goldman Sachs might want to headhunt people currently at Citi, and vice versa. Doing this at any kind of scale can't be done easily on LinkedIn, so Alumnify has an opportunity here.

## Growth Hack Ideas

The question is: how do we quickly and efficiently get Alumnify in front of all of these profiles? One way is to use Alumnify itself to find them.

- In a cold email to an alumni relations director, call out what school they went to. Tell them they could send messages just like this to all of their alumni.

- Send a message to a newly-hired digital marketing director congratulating them on their new position and suggesting that they check out Alumnify.

- Pitch recruiters a list of all Google alumni who went to Stanford.

Then there are the associations, the opportunities where we can hit a bunch of these guys at once. There's an (https://www.case.org/conferences-training/alumni-relations-institute-2023) that would be a perfect audience for Alumnify. There's a million LinkedIn groups and YouTube and blogger influencers looking for new growth marketing hacks. I could offer them free usage in exchange for a testimonial or pitch. For recruiters, I'd also look for LinkedIn groups and try to win a few over with InMail and social media hits.

On the organic side, I've already started to make the company and school detail pages more SEO-friendly. Alumnify needs marketing pages, though. It needs help showing off how it works. The way I built it, Alumnify is able to link directly to a company or school detail page. I should show off a few on the homepage.

SEO isn't really a growth hack, but it's important nonetheless, and forms the basis of any good growth recipe.

## Conclusion

I like Alumnify. It was fun to build. It should exist in the B2B sales and marketing data ecosystem and Live Data should be the company to put it there.