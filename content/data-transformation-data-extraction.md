Title: Data transformation >> data extraction
Date: 2023-05-26 13:51
Slug: data-transformation-data-extraction
Category: Technology
Tags: data engineering, business strategy, etl, technology
Summary: Why data transformation creates more market value than extraction in the ETL framework, using MightySignal and AppMonsta as case studies.

The ETL (Extract, Transform, Load) data framework has been around for a long time. Its roots formed in the early days of data warehousing in the 1970s and 1980s when solid-state drives (SSDs), which use a technology commonly known as flash memory, first hit the market. You might remember the computer hard drives that buzzed, clicked, and hummed when you loaded a program. That technology involved a rotating disk with an arm like a record player that read and wrote data to the disk. It was relatively slow and impossible to scale down. There'd be no "thumb drive" version of this technology.

The SSD revolution quickly drove down the price of storage, and with it, emboldened companies to grab and retain more and more data. The ETL framework evolved as a logical way to deal with this mass of information. You take raw data (in the Extract stage) and make it useful (in the Transform stage) and ultimately throw it into some publicly accessible API or feed (in the Load stage).

You take raw data, wrangle with it to make it nice, and then put some sort of interface on it so other people or companies can use it. That's all pretty obvious. What's less obvious, and what I've come to appreciate in the last few years, is that these steps are not valued equally by the markets.

({filename}mightysignals-new-leadership.md), the last company I ran, was an extraction company. We extracted the type of software running in mobile apps. We also transformed and loaded it, but we did so in a way that kept it in the same extracted context. That's a bit nuanced, but suffice to say, I'd still put MightySignal squarely in the extraction bucket even though we did some transformation and loading for our customers. 

MightySignal acquired [AppMonsta](https://appmonsta.com/). This was also an extraction company that took app details off of the app store pages and loaded it into an API. Yes, there was also a little T and a little L here and there but primarily AppMonsta was an extraction company. 

An extraction company is one that spends most of its resources on extraction. Even if it does some T and some L, if most of its resources are spent on extraction, then it's an E company and has the mixed bag of pros and cons of doing data extraction.

The critical insight I want to focus on here is that E companies don't produce as much enterprise value as T and L companies. Enterprise value is shorthand for the valuation of a company, which is a function of the company's revenue, market, and growth rate. The factor that I'll focus on here is revenue. I argue that E companies don't make as much revenue as T and L companies and therefore have a lower enterprise value. 

There are a few reasons why E companies don't make as much revenue. Let's break them down. 

## Extracted data is a commodity

There's nothing special about extracted data. It's usually hard to get, and I'll consider that difficulty later on in this post, but once you have it, it's a commodity: it looks just like everyone else's extracted data. That's the nature of extraction. Anyone *can* do it, but not everyone *wants *to do it. Once you've extracted the data in its raw form, it's going to be the same product as if I'd done the extraction myself. You may be better at it than me. You may write better scrapers or have a better server architecture, giving you a competitive advantage, but the end result is going to be the same as if I scraped it myself. 

Therein lies the challenge. Raw, extracted data is a commodity. It's undifferentiated; I could buy it from multiple sources, and likely will choose the source based *purely on price*. In a mature market, quality is going to be the same between sources, so consumers buy the cheapest option.

Markets with pricing pressure are difficult environments to produce enterprise value. Investors don't like them. They are the realm of nail salons and convenience stores in the real world. In tech, they are data extraction and, increasingly, B2B SaaS companies. These can make great lifestyle businesses, but they're not likely to produce venture-scale returns. When competing products start to look the same, it's time to either innovate or accept a lower valuation. 

## Data extraction is a distraction

Data extraction companies have a very hard time being great at both extraction and transformation. The complexity of data extraction is a bit of a moat; it's why I'd rather buy than build, so there's a business to be had, but once you're in the extraction business, it's hard to leave it. 

Running an extraction operation is playing non-stop wack-a-mole. The fire drills are constant. There's no time for transformation when all of your resources are focused on keeping the scraping operation alive and expanding it in a constantly evolving landscape. 

This distraction makes it hard, if not impossible, for an extraction company to also do the creative, innovative work of transformation that creates unique additional value. All the attention has to be on extraction because it's so darn complicated and fragile. 

Tying this back to revenue, it means that extraction companies have a hard time adding value that they can use to justify higher prices. It's hard to grow revenue without increasing prices.

## Data extractors sell to data transformers

I have some experience with the nature of this market. Like I said, both MightySignal and AppMonsta were extractors. We both sold to businesses that transformed our data into new products by combining datasets, exposing them in interesting ways, and adding user management and billing features required by enterprise customers. 

As a result, our customers grew much faster than we ever could. By creating a unique data product and enterprise features, they were not price-constrained. By not being price-constrained, they could innovate. By innovating, they could continue to drive enterprise value upward with higher prices. This is the positive cycle that we lacked as a data extractor.

Data transformers need data extractors. They don't want to do the extraction themselves for the reasons I described above. This creates the market for data extractors, but it also keeps them at lower valuations than data transformers.

---

As I've ({filename}platforms-versus-point-solutions.md), Shovels will be a data transformer. In that blog post, I described this same idea in terms of a platform versus a point solution. Here, I would describe data transformation companies as platforms and extraction companies as point solutions. I want Shovels to be a platform, a transformer, a unique provider of data, but without commodity pricing pressure. I want to innovate and create enterprise value that is attractive to venture capital firms. 

I recently [our April 2023 newsletter](https://www.shovels.ai/blog/april-2023-newsletter/) in the Shovels blog that we raised $1M. I wouldn't have been able to raise it without describing Shovels as a transformation company. I know this because my original pitch was extraction. I didn't know we had the option to buy permit data, so I had to lead with this extraction focus. I could get first meetings, but none of the investors wanted follow-ups. When I discovered that raw permit extraction was available to buy, I changed our pitch to be transformation-focused. Investors leaned in and we pretty quickly identified our lead. Angels followed, and then more funds. The transformation pitch was far more compelling than the extraction pitch. 

To be clear: I'm glad data extraction companies exist! I'm grateful for them and I have nothing but love and respect for the ones that do it well. They're important and they can make great businesses for the founders, but I have other ambitions this time.