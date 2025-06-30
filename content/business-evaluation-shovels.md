Title: Business evaluation: Shovels
Date: 2022-11-22 12:04
Slug: business-evaluation-shovels
Category: Business
Tags: business evaluation, data platform, construction, shovels

*TL;DR I'm now working on (https://www.shovels.ai)*. 

I’m going to evaluate a business that I’ve already started working on. Perhaps I should have done this earlier, but for better or worse, this project has evolved far faster than expected!

To back up a bit, I’ve been looking for a good idea for a while. I was obliged to stick with MightySignal for a year after Airnow acquired it. I set a timer in July 2021 thinking it would be easy to figure my path out in the following year. 

But COVID dragged on, I continued (https://rbucks.com/2020/10/24/im-now-an-adjunct/), and life simply just kept moving. The year was up before I knew it. I wrote (https://rbucks.com/2022/06/22/business-evaluation-clime/) in June 2022, just four months ago. In it, I said I’m a “general manager in search of an idea” and that I wanted my next idea to be a “B2B climate tech solution that solves an enormous problem.” 

The idea was elusive, to say the least. I crawled through the thousands of posts on (https://workonclimate.org/), social media-stalked my contacts launching  their own climate tech companies, and went deep on at least three co-founder opportunities. I came close to joining an electric vehicle manufacturer (micro-mobility, like golf carts), a carbon-free steel technology, and a programmatic interface for carbon accounting. 

None of them worked out. Either I fell out of love with the idea, the CEO/co-founder I was courting chose someone else, or momentum waned and sputtered out. 

And then, out of the ether, I started thinking about home construction and contractors. My wife and I did (https://rbucks.com/2021/11/14/how-we-did-our-home-addition-and-remodel/) and it went really well. Our neighbors had the opposite experience. I felt bad for them, angry at the guys they hired, and wondered what the difference was between the contractor we hired and the one they went with. I started to look around and idea began to materialize. 

There’s public data about building permits and the inspections that are required for a permit to be signed off. There’s a ton of this data, in fact, but it’s hard to get. Despite being public, there’s no standardized, simple interface to interact with it. There are a dozen different softwares among the jurisdictions that post the data online. Many simply don’t have it on the Internet. 

A little antenna went up in the back of my head. This is why there’s no single, central, public database. This data is super fragmented and painful to get. I like fragmented data. I like relentlessly painful scraping projects. I can do this! 

For a month or so, I did nothing. I told my neighbors about it and they nodded in appreciation of my excitement if not for the brilliance of the idea itself, and then as has happened for my preceding forty years, life just rolled along. 

A change happened in mid-August when I brought a group of friends (https://rbucks.com/2019/03/03/my-happy-place/) for a weekend. It was a short trip, just one night for most of the group. Two close friends stuck around while I put the cabin back together and as I swept the deck they gave me a very consequential pep talk.

I don’t remember exactly what was said, but I remember what I took away from it:

- I can be a great CEO. I can lead and navigate a business. 

- I can assemble a great team. Great people will follow me. 

- I can fundraise. People will trust me with their investment. 

They gave me a big pat on the back and said they both see me being a successful CEO of a climate tech company. “It makes all the sense in the world,” one of them said. They agreed that I should chase after this dream. I sighed, smiled on the inside, and kept sweeping. 

I returned home invigorated. I reached back out to a couple of the co-founder conversations I still had open. They both quickly ended. Undeterred, I posted a project on Upwork to get help building the permit scraper prototype. It felt great to start moving. 

Then I reached out to a contact at (https://www.teamworthy.com/) who I’d known for years. He had also encouraged me to pursue my own company rather than working for anyone else, including another turn as a hired CEO. I sent him an email to reconnect and told him about the carbon credit accounting opportunity and my idea to harvest building permit data. A week later, the carbon accounting deal was off the table and I was left with my permit data idea. 

I scheduled a meeting with my Teamworthy guy. He told me that to be competitive with their process I needed a co-founder. Fortunately, I had the perfect person in mind. 

I met Luka for the first time in February 2020 when I organized a (https://rbucks.com/2018/11/02/mightysignals-new-leadership/) retreat in Las Vegas. We rented out the “Real World Suite” at the Gold Spike in Downtown Las Vegas so everyone could stay in the same place and get more opportunity to connect (in retrospect this only worked because we were all guys). 

Luka arrived last due to a harrowing sequence of flight delays. He ended up traveling nearly 24 hours from Slovenia to Las Vegas. I felt terrible for him but he was chirpy as ever, just glad to be there, and went immediately to sleep. 

That trip almost didn’t happen for another reason — in order to get Luka there, I needed to close the acquisition of AppMonsta, the company he was running at the time. Legal delays forced Luka to hop on a plane uncertain if the parties would have everything signed by the time he touched down in Vegas. That too had a photo finish. Docs were executed and the wire triggered just hours before Luka took the elevator up to the suite. 

I would come to admire Luka and Cata, his support engineer, greatly over the coming years. They worked hard, constantly putting out fires as the goal posts were in constant motion. 

The goal posts, in this case, were the Google Play and Apple App Stores. AppMonsta performed daily scrapes of both, each with millions of pages. Doing this at scale, non-stop, with monitoring and redundancies, is a really difficult task. That AppMonsta could do this with such a small team was truly remarkable. As an important plus, both Luka and Cata fit very well culturally with my small crew at MightySignal. I was grateful that they both stayed with me through our Airnow acquisition about a year and a half later. 

Due to some issues at Airnow, Luka left a few months ago. We lost touch for a bit and I reached out in late August 2022 to ask him for help with my permit scraper. We had a brief chat and then a few weeks went by. Unsure if Luka was interested, I continued to work with my freelancers. 

We finally reconnected at the end of September and I told him that I put him in my pitch deck as a co-founder. He didn’t object, and we’ve been working together since.

Now, long backstory aside, let’s dive into the actual business. 

## **The Problem ** 

As I wrote in the (https://www.shovels.ai/blog/introduction-to-shovels/), there’s an agency problem in the trades. Contractors have far more knowledge about their skill level and fit for a job than the people who hire them and the banks who fund them. As a result, there is an inefficient market with a lot of bad deals. This is how my neighbors ended up with their awful contractors. 

Which contractors are active in my area and which of them are the best fit for my project? The answer today is “nobody knows!” This is what we call the contractor agency problem. Everyone looking to hire a contractor, whether they’re a homeowner with 2,000 square feet or a real estate builder with 2 million square feet, has this problem. The financial institutions who loan money to builders have this problem, too. 

There’s another problem, and it’s faced by planners and data aggregators who want to understand building trends in a specific geography. The geo could be a zip code, county, state, or even just a single address. 

What specific type of building activity is happening now and has happened in the past in this area? The answer, again, is “nobody knows!” I spoke to an executive at a very large home improvement website recently. These guys have raised hundreds of millions of dollars and should have the resources to acquire any dataset they want. He told me they are looking for a way to get permit histories on any address in the US. He said it’d be a really big deal for them to get this. 

But it doesn’t exist… yet. 

## **The Solution**

(https://www.shovels.ai) (did I mention that’s what we’re calling this business?) figures out where construction work is happening and who’s doing it. We pull together and analyze millions of records of public data on building permits and inspections. From this data we can measure and therefore predict performance for every contractor, and we also see what work has been done on every address. 

What we’re seeing already is not surprising. The data is messy: it’s incomplete, it’s inconsistent, it’s rife with human error. It's every dirty data problem wrapped up in one incongruous mess. Luka and I remind each other that this is our moat. This is the essence of the problem: decentralized data with different schema maintained by different organizations. 

This is why the world needs Shovels. 

But more specifically, the world needs Shovels because the world needs more information about who the good contractors are. By analyzing inspection data, we're able to introduce a couple of new metrics into the contractor hiring process. As I describe on (https://www.shovels.ai/banks), our first two new metrics are:

When we make a histogram of all of the inspection pass rates for contractors in Contra Costa County, it produces a beautiful bell curve.

!(https://rbucks.com/wp-content/uploads/2022/11/rate-1.png)

This is exactly what I'd hoped to see. The standard deviation is about 13 points on either side of the mean. Those contractors beyond the standard deviation are the best (right side) and worst (left side) of the bunch, and we can raise that flag to anyone looking to hire them. It doesn't necessarily mean they're awful, but it does mean that hiring or funding them has additional risk. 

Beyond this positive/negative rating system, we can also match contractors to future jobs by showing specifically which type and size of projects a contractor tends to excel at completing. We're able to grab all the metadata along with the permits to visualize the types of projects a contractor has done recently. We also can share how many jobs they tend to do at once. This is useful to make decisions about both hiring and funding.  

Our solution addresses the data transparency problem in construction. Specifically, provide visibility into what construction activity has been happening. By looking at that problem, we also end up with info about contractors, so we can solve the contractor agency problem.

We are building this database for the first time. It doesn’t exist today, and to me, this is really, really exciting. My past projects involved rearranging existing technologies and commoditized data. This is the first time I’m building something truly original. 

So that’s the problem and what Shovels does to address it. Now let’s dive into the business itself. 

## Business Model

Here I'll explain how Shovels grows to $10 million annual recurring revenue (ARR). 

We sell data to banks, builders, and construction data aggregators and make it accessible through a web application. We price based on geography. Here's our current rate card:

- Single jurisdiction (county or city): $500/mo

- Ten jurisdictions (bundled by us or custom): $2,500/mo

- All jurisdictions: $500,000/year

Our base fee will include one year of historical data. We will charge additionally for all historical data, which might go back 10 years or more. We also charge additionally for API and data feed access.

With an average contract value (ACV) of $10,000 per year, we can get to $1 million ARR with just 100 customers. If ACV stays constant, it will take 1,000 customers to hit $10 million ARR. 

So, how do we get to 1,000 customers? There are about 3,000 counties and 350  metropolitan areas in the United States. Revenue should scale with geography, so if we were in only 100 counties, we'd need to get an average of 10 customers in each one. If we focused on the major metro areas, say the top 10, we would need 100 customers per metro. 

This requires real work on both the sales and engineering sides of the house, but it is reasonable. Plenty reasonable. And it doesn't take into account the likelihood of signing some major nationwide contracts that would each be worth 50X our ACV. 

The harder question is how we get to $100 million ARR. This revenue level is approaching IPO territory and one where Shovels could be valued at $1 billion or more. This breaks down as follows:

- Data coverage in 100% of metro areas

- Data coverage in 90%+ of counties 

- 10 national customers at $1M per year = $10M ARR

- 50 customers in each metro at $5K per year = $90M ARR

It adds up fast! The trick, of course, is that we need to *be* in each metro before we can collect revenue. Thus, we'll have to absorb engineering spend ahead of revenue. This is our primary case for venture capital. 

## Use of Funds

I used to struggle with this section in my previous companies. The use of funds was never clear-cut. I felt like I had to make up reasons to spend money. For most of my projects, the software was not ground-breaking stuff. We attempted to turn it into some very complicated work, but in retrospect very little of it was necessary. 

Likewise, on the sales and marketing front, we built up expensive sales teams and purchased expensive marketing software long before found product-market fit. We did this because we could, because the money was there and we were expected to spend it. 

Shovels is different. There's a clear connection between engineering and sales expense. We need to harvest data (engineering) in order to sell it (sales). The two work in tandem, at least until we have complete coverage. Even then, there will be more local datasets to harvest, integrate, and analyze. I can see engineering and sales working together well into the later stages of this business.

I'd like to raise $1M sooner than later. Here's how I'd spend it. 

Initially, Luka and I figure a team of 3 engineers can add five jurisdictions every quarter. A jurisdiction is a city or county that manages permits (most cities outsource this to the county; very few run their own permitting operation). A good benchmark for a metro area is five jurisdictions, so this engineering trio can add one new metro area to Shovels each quarter. 

Our engineers, a couple of revenue folks (sales development representative and marketing manager, perhaps) plus founders would take us up to about $1M per year in expense. Now, we back into the four metro areas and 20 jurisdictions we'll have in Shovels at this point, and assuming the $10K/year ACV holds, we need each metro to contribute $250K per year, or about $20K per month. 

That's 20 customers in each of these four metro areas. Think about how many banks and construction companies there are in San Francisco, Chicago, Tampa Bay, and Dallas. Can we get to 20 customers in each one? You betcha. 

I want to raise $1M in order to get $1M ARR. That's the ratio I would promise to investors. Every dollar raised gets a dollar of ARR within 12 months. 

That's my north star as CEO. Since I think we can achieve it, I'm all-in. LFG!