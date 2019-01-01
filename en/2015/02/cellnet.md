# Cellnet

Most of us know that our phones can connect to the WiFi hotspots
around us [..] What few people realize is that two phones can often
see each other, and chat, over these hotspots. In other words, without
using any broadband, and without any traffic going out over the public
Internet.

This is called a "client-to-client" connection. Client-to-client connections work on most WiFi access points (that is, the little box with antennas that creates the hotspot) that you buy, and most that you'll find in cities. There are exceptions. For example the AT&T hotspots in Starbucks across the US do not allow client-to-client connections.

If you think this through, you may see the possibilities. When you are at home, or in the office, or in a café with a friendly WiFi hotspot, you can connect a bunch of phones, tablets, and laptops together in interesting ways. This is not a hypothesis. There are applications that stream video from a phone or tablet to a WiFi-enabled TV, or a TV with some dongle, like Google's Chromecast, attached. In 2011-2012, my firm designed such technology for a large electronics firm, and it's in use on their smartphones today. I also wrote an open source library called Zyre that does this -- if you run it on a phone, it will look for any other phone also running Zyre, connect to it, and then let applications exchange data.

When you are out and about in the street, things become more fun. It's harder to find friendly WiFi hotspots. [.. But a]ll modern smartphones -- since 2010 or so -- can create their own WiFi hotspots at will, unless the ability has been disabled by the phone company. AT&T, for example. So if you have a smartphone in your pocket that is running Zyre, and you're walking in the street, it would be possible to switch on your WiFi hotspot, and search for other friendly WiFi hotspots, and make opportunistic connections to any other Zyre smartphone [..]

If you imagine a group of friends hiking in the mountains, their smartphones could connect to create a small "cell," to use the terminology of mobile phone networks. However, when the same people are in the city, in a bar, or in a demonstration, at a concert, or even at home, they will be in range of several cells.

The cells aren't fixed like mobile phone cells. Instead they switch on and off and move about randomly, since each cell is centered on one smartphone acting for a while as a WiFi hotspot. Now, a smartphone can be in one cell at a time, and as it moves from cell to cell, it can carry information with it. This creates an "asynchronous mesh," in other words, it's possible for data to move across an entire city, slower than we're used to with broadband, yet still fast enough to be useful.

Let me give an example. A woman takes photos of the police arresting a protester. As she takes these photos, they are pushed out to other smartphones in that cell. Those smartphones move away from the scene, and the photos flow over several more hops, and eventually have reached several thousand smartphones across the whole downtown area. It is impossible to know the origin of the photos, impossible to censor them except by physically seizing all phones in the area. That's hard, as they don't have to be visible in order to join a cell.

As people move around the city, the fabric stretches wider and wider. In order to cover the globe, however, I'd exploit those fast-but-stupid broadband connections we all have at home, and create temporary virtual pipes between random pairs, each end of the pipe in a different city. So my PC would connect to a peer in Toronto, then in San Diego, then in Kuala Lumpur, and so on. Modern PCs, fat up from too much gaming, can handle hundreds of such pipes at once. We'd secure and encrypt the pipes using throw-away asymmetric keys. Everything sent on the pipe would be stripped of metadata.

That gives us a global fabric, which I'll dub the "Cellnet." The Cellnet is slow, asynchronous, opportunistic, and works at a human scale, closely tied to our physical movements and proximity to other people. It is a different animal from the Internet we use today, where distance is abstracted to nothing and you never really know who you are talking to. I like the idea of de-abstracting technology.

All of this is possible today, in software, and could take advantage of improvements in hardware and firmware, such as real mesh networking and better batteries. We could build cheap dedicated devices that run the Cellnet: a pocket-sized box that is all battery, with powerful radios, and a couple of blinking lights just because. No screen, no fancy UI software, just a pocket-sized Cellnet node. It could double as a battery recharger for smartphones, which gives plausible deniability to anyone arrested with one, when they are banned. Kickstarter, anyone?

The Cellnet would be extremely hard to spy on or disrupt. It is possible to capture WiFi traffic by being physically very close. However it's also quite easy to secure traffic between two peers to the extent that it cannot be read or modified or faked. The only way to get information is then to seize the phone itself. While physical seizures (including the old "beat them until they talk" technique) are always an option, they do not scale to billions of people. The spy state can still tap into traffic that goes across the Internet, by acting as Cellnet nodes. However it can get very little useful from it, and crucially, cannot tie activity back to individual actors.

The Cellnet isn't fully resistant. One can attack WiFi hotspots by sending out jamming signals. However this will disrupt more than just smartphones, and it means having equipment in the right place at the right time. That is difficult and costly, and security is always about raising the costs to attackers.















