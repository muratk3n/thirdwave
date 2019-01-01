# Tendermint

Satoshi created a spark with Bitcoin, but the future is in Tendermint. Research in decentralized consensus algorithms has been in progress since the early '80s. Today we have the ubiquitous and powerful computing network to run a decentralized blockchain ledger, and thanks to Bitcoin and the cryptocurrency community all the pieces are in place to redefine the nature of finance.

What makes Tendermint special?

At today’s Bitcoin prices and reward schedule, miners are rewarded on the order of $1,500,000 a day to secure the blockchain ledger — and a significant portion of that money is wasted on electricity.

Proof-of-work based consensus algorithms are also slow, requiring up to an hour (or more for large transactions) to fully confirm a payment to prevent double-spending, and the forking nature of the blockchain makes applications difficult to implement correctly.

Tendermint solves these problems because it solves the long-standing “nothing at stake” problem. The solution is comprised of two parts.

First, we use a Byzantine consensus algorithm to agree on the next block.

We choose the DLS algorithm for its simplicity and ability to tolerate arbitrary disruptions in the network. This algorithm doesn’t incentivize nodes to waste electricity. Instead, it requires nodes to securely sign messages while participating in a round-based protocol.

Tendermint introduces a few innovations on top of the DLS algorithm to make it suitable for the blockchain, and for completely decentralized P2P gossip networks (like Bitcoin).

Second, we disincentivize validators from forking the blockchain.

Users must first post a bond deposit before becoming a validator to participate in the consensus process. To get the bond deposit back, validators must post an unbond-transaction and wait a long duration of time.

If the validator causes the blockchain to fork while its coins are locked in bond, all of its coins are destroyed. This means that as long as you sync your blockchain with the network periodically you never have to trust a central checkpoint.

Tendermint is both a decentralized organization as well as a foundational technology.

We believe that the future is comprised of many interconnected-but-sovereign blockchains that serve different purposes for a variety of communities. Tendermint will be the leader driving innovation to bring interoperability.

Tendermint the decentralized organization is comprised of all the users and contributors of this foundational blockchain technology. Our first prototype network will be a blockchain ledger that represents our community. 












