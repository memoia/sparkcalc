In response to "EngineeringManagerChallenge\_(1).pdf"
======================================================================

(sent by taek=sparkcentral.com@greenhouse.io on Tue, 04 Aug 2015 02:04:32 +0000)


## Assumptions

* Existing software solution, while closed-source, provides or can
  provide access to its data (i.e., through an integration API, or flat-file
  exports, or direct access to underlying data store).

* Existing software solution provides the current requirements of the product
  catalog and online payment acceptance, less the shopping cart feature.

* New features, such as the shopping cart, will require a complete replacement
  of the current catalog software, but not within the first six months
  allocated for the development of the cart.


## High-level requirements for MVP (non-exhaustive)

* As a user, I want to add as many items and variants to a cart as I can.

* As a user, I want to be able to edit my cart: select quantities, delete
  items, and "save for later."

* As a user, I expect to be able to return to my cart after closing my
  browser, or resume using my cart on another device.

* As a user, I would like to be able to review my cart prior to checkout.

* As a user, I want to be able to see what's already in my cart alongside
  product search results, such that I don't add the same product again;
  I would like to be able to have the opportunity to edit/remove the item
  too, within this UI context.

* As a user, I would like to be able to search for products by standard
  identifiers (like UPC) as well as product-specific search identifiers.

* As a user, I would like to see related products in my search results.

* As a maintainer (i.e., Engineering and DevOps), I would like appropriate
  monitoring in place for all portions of the stack involving catalog
  integration layer and cart usage, to make diagnosing and fixing problems
  faster and easier.

* As a maintainer, I would like a load testing suite in a simulated production
  environment so that I can have confidence that the application will perform
  under initial and subsequent load expectations.

* As a maintainer, I would like an integration test suite that I can run prior
  to release that proves the cart functions as expected.

* As a maintainer, I would like a simple architecture to start with, having
  minimal moving pieces to make diagnoses easier.

* As a maintainer, I would like an architecture that is designed with
  large-scale load balancing and "cloud infrastructure" in mind (say,
  AWS, AppEngine, etc).

* As a business, I need metrics on cart use and performance.

* As a business, I need the cart to integrate with the rest of my product.

* As an engineer, I would like high-level must-haves, nice-to-haves, and known
  future requirements firmly agreed upon prior to work beginning, with the
  understanding that most future requirements will be unknown.

* As an engineer, I would like to be able to run the entire stack in a local
  environment and be able to easily load fixture data for various test cases.

* As an engineer, I would like regular scheduled meetings with product
  stakeholders to show progress and collect feedback.

* As a UI designer, I, too, would like regular scheduled meetings with
  stakeholders and with engineers, to ensure that unplanned but required
  user interfaces are agreed upon by all parties.

* As a product stakeholder, I would like the engineering team to provide
  regular metrics about the state of the product, including bugs found early
  in the development cycle, such that I can help guide priorities and manage
  business expectations.


## Migration to new catalog/payment system (non-exhaustive)

* As a merchant (currently, a set of users within the company), I would
  like to be able to edit my products' standard attributes (such as images,
  UPC, variants) as well as meta-data about the product (i.e., keywords,
  categories, descriptions).

* As a merchant, I would like to be able to accept multiple forms of payment
  on a system compliant with PCI-DSS, with minimal added cost per transaction.

* As a maintainer, I would like a set of services that fill the requirements
  of the existing product catalog software, and remain distinct from the
  shopping cart.

* As a maintainer, I would like an interface to the replacement catalog
  services that is backwards-compatible with the previous integration.


## More on Architecture

* Try to follow the "12-factor app" (12factor.net) recommendations.

* Provide team with leeway on how to approach problem.

* Requirements:
  - Needs to be able to "horizontally scale"
  - Needs metrics, log aggregation, alerts
  - Make use of SOA strategies where appropriate.
  - Start with minimal moving parts / services to meet requirements.
  - Needs to have a predetermined designated growth path for further scale.
  - Should include failover and "hot" recovery solutions.

* Infrastructure should probably include:
  - HTTP load balancers
  - Web servers running main apps
  - Application servers running long processes
  - Jobs instance for "cron"-like scheduled tasks
  - Relational database
  - Document database with full-text search (later on for catalog replacement)
  - CI instance
  - Central code repo hosting
  - Message queue service for long-running processes, including job monitoring
  - Provisioning/automated deployment
  - Centralized logging
  - Awareness of multiple environments (i.e., local vs. deployed)

* Services might include:
  - Users
  - Shopping cart
  - Browser event / Websocket listener
  - 3rd-party integrations (integration with existing catalog; later:
    integration with payment processing system)
  - Product catalog (later in year)


## Engineering culture/practices

* Should have good test coverage across all aspects of product.

* Pair programming encouraged for large features.

* Code reviews - must occur prior to shipping. Focus on:
  - Logic errors
  - Style ("as a reviewer, do I understand this?")
  - Design ("does this deviate from our practices or previous decisions?")


## Hiring roadmap

* Find two engineers with direct or related experience.

* Initially, outsource UI design or hire a UI expert on a contractual basis.

* After core features/architecture is complete (enough to diagram and begin
  local development, say, no later than 3 weeks into the project), find a
  DevOps person to work on deployment and load testing.

* After architecture is revised to accommodate expected load (determined through
  consultation with business, with revisions expected to be minimal; no later
  than 3 weeks after findings from initial load tests), find a QA person to
  develop integration and functional test suites.

* After this, find a specialist for core portions of the stack to assist with
  fine-tuning, metrics, and general/unanticipated engineering challenges.

* If, over the course of a few months, the team determines a separate
  project/product manager would be helpful, bring one in on contract.


## Cultural values and expectations from all team members

* Expectation to communicate, be responsive, transparent.

* Expectation to be mindful and respectful.

* Expectation to prioritize pragmatism over creative solutions.

* For engineers, expectation to organize code in a way that enables the team to
  easily grow without excessive institutional knowledge transfers.

* Expectation to document metrics regarding time spent on work. For engineers,
  this includes time spent on certain modules, bugs, and refactorings to address
  new requirements or performance findings.

* Expectation to be generous with time to other teammates.

* Subscribes to team mentality around delivery of product; compromises with
  others.

* Can both teach and learn, and desires a culture where this exists.

* Considers long-term business needs when making design decisions and discusses
  these concerns with team.

* Seeks feedback.

* Humble, stable, methodical.


## Interview process

* Intro call.

* Take-home exercise.

* In-person exchanges. Determine:
  - Interests
  - Personality fit
  - Experiences (and what was learned from them)

* Pair for a day with relevant person if applicable.

* Collect team feedback on candidate (i.e., team-player? demonstrates humility?
  easy to work with? learned from previous challenges? is skilled enough for
  position?)

* Final discussion as team regarding candidate's fit, and where candidate would
  best be placed. Determine with team who will help with the onboarding process
  and how, should candidate accept offer. Determine with team what projects
  candidate will initially contribute to post-hire.


## Day-to-day processes

* Daily check-ins for blockers.

* Weekly reviews of progress with product stakeholders.

* Design decisions and rationales are documented in a central location.

* As team grows, determine if more structured project management is appropriate,
  and come to consensus with team what workflow makes sense.

### Relationship with product team / stakeholders

* Weekly reviews with engineering team.

* Maintain living document of metrics regarding team progress, challenges,
  deviations from plans (with rationales.)

* Provide regular "digest" updates to bosses derived from living document.

* Continue to flesh out high-level roadmap and seek feedback, reprioritize as
  needed.

* Continuously inquire with product team regarding unanticipated issues,
  providing recommendations from engineering team up front.

### Manager role

* Find ways to unblock team.

* Assist with finding ways to parallelize work.

* Reprioritize stories/efforts as needed.

* Shield engineers from chaos; help reduce context-switching to improve focus on
  particular requirements.

* Proactively schedule weekly one-on-ones to review goals, discuss team issues,
  seek feedback, etc.

* Review code to stay familiar with how product works.

* Monitor how things are going and communicate to appropriate
  channels/stakeholders.


## Wild-guess Budget

* Assume ~$400k for initial hires (for first six months)
  - Two engineering generalists, offered max $150k/year
  - One sysadmin, offered max $120/year
  - One QA specialist, offered max $110/year
  - One engineering specialist, offered max $170/year
  - Contractors (UI, other), max $50k for this period

* Assume $10k for initial equipment costs (say, $2000/workstation)

* Assume $5k/month for external costs (i.e., production hosting,
  any needed 3rd party services, etc), or $30k for first six months

* Estimate weighs in at $400k for first six months, leaving wiggle-room
  for unanticipated expenses.

* Assuming no changes, this leaves just over $300k unallocated for the
  remainder of the year, enabling full-time hire of contractors and
  additional engineering staff for the build-out of anticipated
  catalog / payment system replacement.
