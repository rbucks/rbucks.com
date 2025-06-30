Title: My $524,687 side hustle
Date: 2017-07-24 09:41
Slug: my-524687-side-business
Category: Business
Tags: entrepreneurship, side-business, toofr, parallel-entrepreneurship
Summary: The complete story of building Toofr into a $524K side business while working at Scripted, learning to code, and pursuing parallel entrepreneurship.

By the time I (https://medium.com/@rbucks/whats-next-for-me-a6418447d3d0), its lifetime Stripe revenue was in excess of $524,000 with monthly recurring revenue (MRR) (http://nathanlatka.com/thetop610/).

That’s great revenue for a project I spent just a few hours a week on over the last few years. It’s also why I’m so excited to have the opportunity to put full-time energy into it now.

#### Origin story in brief

It started with an observation: most companies use the same pattern for their employees’ email addresses. A typical startup uses the first_name@company_name.com pattern. My email address at Scripted was ryan@scripted.com. My email address at Toofr is ryan@toofr.com. No surprises there.

The most common email pattern, based on the millions I’ve stored in the Toofr database over the years, is actually first_initial_last_name. When we hired interns at Scripted I’d set them up using this pattern so we could save the first_name pattern for permanent hires. I also set up a rbuckley@scripted.com alias just in case I needed it.

This was the technique we used to build cold email lists on the sales team at Rapleaf (acquired by Tower Data) back in 2011. I was learning to use Python to scrape websites and guess emails. When I left Rapleaf to go back to my (https://en.wikipedia.org/wiki/Scripped) and help it pivot to become (https://www.scripted.com), that same email list building technique was our primary lead source. I also continued to consult for Rapleaf to supplement my early (very meager) Scripted salary, further enhancing my Python scripts and sources.

Around this time, in late 2011, I was getting very anxious to learn how to build web applications. I watched our team build the screenwriting app and I could get my hands dirty with HTML and CSS, but was completely in the dark about how the web app itself worked. Scripped was built in JavaScript and PHP. The web framework was CodeIgniter, one of the first popular model-view-controller (MVC) frameworks. I read post after post about MVC but I couldn’t fully wrap my head around it. I decided the only way I’d learn it was to build a damn app myself.

If I only had an idea… Aha!

#### Learning to Py

Throughout 2012 I completely re-wrote those Python scripts, hooked them into CodeIgniter (after many a gut-wrenching, hair-pulling night), put up a subscription wall, and launched (https://www.toofr.com) to the world in March 2013. (That month it made $285 in subscription revenue.) In 2016 I rebuilt the entire application in Ruby on Rails and in 2017 I migrated the whole thing from a (https://www.linode.com) cluster (https://www.toofr.com/articles/why-toof-uses-heroku-for-its-email-finding-service). I managed to take Toofr down only a handful of times; the longest probably was a harrowing two-hour outage. I’d completely fudged the database but managed to restore from a backup with only a little data loss.

Those are the nights when you earn your engineering stripes.

There’s no secret to learning how to program. You just do it, and when you run into problems, you google them. And when you google them, you’re very likely to land on this godsend of a platform called (https://stackoverflow.com/). That’s the real answer to how I learned to program: googling my many many questions and finding the answers, code samples and all, on Stack Overflow.

By the time Toofr made its first money, I’d become proficient with the following:

- Ubuntu server and basic Unix/Bash shell commands- Apache web server configuration- Cronjob configuration (I DIY’d a background job processor with this)- SSL certificate installation- DNS zone configuration- MySQL database installation and data importing / dumping- HTML (obviously)- Bootstrap CSS stylesheet framework- JavaScript basics and KnockoutJS framework- Python and specifically its BeautifulSoup parsing library

And that was just the first generation of Toofr. Now I can add to the list:

- Ruby- Rails- Postgres and ActiveRecord (the Rails way to query a Postgres database)- LESS/SASS stylesheet languages- Redis keystore database- Sidekiq background job processing- Nokogiri for website parsing- And my favorite one of all, Heroku, for hosting, scaling, scheduling, monitoring, and basically (https://www.toofr.com/articles/why-toof-uses-heroku-for-its-email-finding-service)

#### A fine line

I continued to work on Toofr at night and on weekends while my real job at Scripted transitioned from internal operations to marketing, business development, sales and eventually into the CEO position. It wasn’t easy, but the secret to a successful side hustle is just consistently putting in the time outside of work. I did it for two years before Toofr started generating significant money. I was busy at work and busy at night, but I relished in that slow-burning grind.

I recognize that it’s tricky to lead a double life as an entrepreneur, but I have a clear conscience about when I focused on Scripted and when I didn’t. For me, Toofr was a release, a way to spend those quiet hours after my wife (and later, my kids) went to sleep that would have otherwise washed away into Netflix streams. It was also a wonderful way to learn to program, something I’d always wanted to do. The feature requests became my course syllabus and the extra income kept me from quitting.

Scripted benefited a lot from Toofr. Our sales reps used it occasionally (and I never charged Scripted) and when we started email marketing again in early 2017, Toofr played a big role. I also think it made me more confident that Scripted should have a subscription model, a process that took me more than a year to convince my team to accept, but we (https://medium.com/@rbucks/the-two-things-i-wish-wed-done-sooner-at-scripted-d45d15a559fa). I wanted Scripted to do it because it was working so well for Toofr, and now Scripted gets more new subscribers every three days than Toofr gets in a month. As it should (see final section).

Toofr has made me a better, more confident entrepreneur. It gave me a skillset I wouldn’t have acquired at Scripted, and my ability to fire up a Rails console and run database queries on Scripted (it’s no coincidence that Toofr’s stack is pretty similar to Scripted’s) also made me more valuable to Scripted.

#### The parallel entrepreneur

People talk a lot about serial entrepreneurs. I’m don’t think of myself that way. I don’t want to run my companies one after the other. Instead, I’ll run them simultaneously, in parallel. Even today, Toofr is not my only project. I have (https://www.enps.co), (https://www.thinboxapp.com), and I’m planning to spin these others up in fast succession:

- A commission calculator to help sales managers and sales ops leaders make fewer mistakes in calculating commissions for their sales reps and SDRs. There are enterprise products out there, but I haven’t seen a good SMB app. It’s a pain I’ve felt personally and I’ve already started outlining a solution.- A group email app that makes it easy to create email lists that recipients can opt in and out from or choose a web-only option. I have a list of about 100 people I’d like to email my Medium content to, but bcc-ing everyone feels spammy, not bcc-ing intrudes on their privacy, and not emailing them at all means they may not see this writing. Some people use Mailchimp for personal newsletters and such, but again, I’d like to offer the option to go web-only. So I’ve started building this too.- A vault for your company email account. As entrepreneurs, we end up with a lot of relationship data in our company email accounts. When you exit, that data goes away. I’m not sure if this is a legal minefield, but I’d like to build something to save the emails and make them queryable forever.- An app that that tracks website changes of your competitors. There are HTML and page diff collectors, but I haven’t seen one that tracks the number of indexed pages, or the site tree itself, and can then give you a heads up that one of your competitors is making a big SEO move. This would give the signal faster than a Moz or SEMRush would. By the time those guys pick it up, it’s already too late.

You might wonder why I’m sharing these ideas. They’re pretty good, right? One truth that will always be a truth and will always be underestimated is building a company is 99% perspiration. It’s a long race and the initial idea is just the first step, so you’re fooling yourself if you think keeping it a secret (going “stealth”) is doing you any favors. It’s not. The only thing you’re doing is preventing feedback, which is a terrible way to start a business. So in that spirit please message me if you like these ideas and want to collaborate! I’d like to get them started ASAP but I have a full portfolio right now.

#### The limits to growth

I’ve recently begun to make other major conclusion about Toofr: as much as I love working solo, and I truly love it, I recognize that there’s a limit to the growth and impact that a one-man company can achieve.

I believe that if I could work with the right team it would have an exponential effect on Toofr, eNPS, and Thinbox. I want to enjoy my ownership and autonomy with Toofr while simultaneously seeing the revenue growth and product development of Scripted. Can I have it both ways? I don’t know, but I want to try.

So in a way I’m writing this as a collaborator dating profile. I kept the provocative, braggy headline because I want to attract others who have done this too and made even more money (I know you’re out there). Please connect!

I don’t want to change my lifestyle, so I’m willing (and in many ways would prefer) to collaborate remotely, with people anywhere in the world. In the meantime, though, I’m content. Toofr’s revenue and growth opportunities are everything I need and more to feel secure and stimulated.

I just can’t help wanting to have my cake and eat it too.