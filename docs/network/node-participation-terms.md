# Node Participation Terms — the Forge Network

**Owner:** WS-011 · **Version:** 0.3 · **Status:** Draft · **Date:** 2026-09-07
**Audience:** public-ready — intended for publication together with the node profile standard;
the content is L1/L2 under D-2026-5, the L3 check has been performed.
**Language:** **The Slovak version is binding; this English version is a translation.**
The Slovak wording is `podmienky-ucasti-uzla.md` (v0.3); both versions carry the same version number and are
changed together.
**Decisions:** **D-2026-14** item 5 (participation terms as a network rule), **D-2026-6** (Forge = a free
platform; nodes that accept orders do business commercially as independent entities), **D-2026-7** ("a contract
through the specification"), **D-2026-16** (a node is not an offer), **D-2026-18** (a node hosts its profile itself
or the platform hosts it on the node's behalf), **D-2026-19** (a node run by a legal guardian), **D-2026-20**
(a capacity has a kind; the same vocabulary for supply and demand) — `registry/decisions.md`.
**Licence:** this text is under **[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)** —
© 2026 Amunet s.r.o.; **the name "Forge", the node network and the node register are not covered by the
licence**. The platform code is licensed separately under Apache-2.0 (repository `forge-platform`).
**Nature of this document:** **a network rule, not a contract.** It creates no obligations and no claims;
it describes how the network works and what it means to be in its register. Related documents:
`standard-profil-uzla.md` (what a profile should contain), `druhy-kapacit.md` (what kind a node's capacity may
be), `forge-platform` (the code that reads and checks profiles).

---

## 1. What this document is for

The Forge network keeps a **public register of nodes**. A node is **a person or an entity that is part of the
network** — it has a public profile and is entered in the register. **A node is not an offer:** it does not have
to offer anything or want anything; whether and when it starts accepting orders is its own choice (the
availability status in the profile). A node that accepts orders **does business in its own name and at its own
responsibility**. Forge is a free platform — it takes no share of a node's revenue and does not run the node's
operations.

**A machine is not the only way to contribute to the network.** What a node can make available is a **capacity**,
and a machine is only one of its kinds — so are transport, space, hands and time, knowledge, material, a digital
asset, legal standing, funding and reach. The kinds are listed in a separate document, **`druhy-kapacit.md`**
(the capacity-kind vocabulary), and **demand uses the same vocabulary** — otherwise the network could never
match the two.

This document says **what it means to be in the register**: what the network expects from a node, what it does
with the node's data, and how a node leaves. It is meant for anyone considering registering their node.

## 2. The node profile is public and belongs to the node

- A node keeps its profile (`PROFILE.md`) according to the **public node profile standard**; it describes its
  capacities there using **kinds from the shared vocabulary**, and if a capacity fits no kind, it uses the kind
  `iné` ("other") and describes it in its own words. The profile reaches
  a public address in **one of two ways**: the node **hosts it itself** (its own repository, website, static page
  or any other public place the network can read — no technology is prescribed), **or the platform hosts it on
  the node's behalf** at the platform's own address. **In both cases the node is responsible for the content.**
- **The node decides what is in the profile.** The profile is the node's document — Forge does not write it for
  the node, does not edit it without the node's instruction and does not comment on it. For a profile hosted by
  the platform, the platform records only what the node supplied and changes it only on the node's instruction.
- The profile is the **only interface** between the node and the network: what is not in it, the network does
  not know about.
- **A node run by a legal guardian** (for example on behalf of a minor): neither the profile nor the register
  **states any personal data of the represented person** — no surname, date of birth, address or town, school,
  photograph, nor the person's own contact; the node carries a first name or a nickname, **the guardian is both
  the contact and the responsible person**, and the profile states that it is managed by a legal guardian. The
  register and the profile are public and permanent, so the rule is observed from the first publication.

## 3. What the platform does with the profile

The Forge platform may **display, download and automatically check** the profile against the standard (shape
compliance: the version header, the presence of the sections mandatory in the given status, permitted values).
The check runs regularly and its result is public — just as the profile is.

A profile hosted by the node the platform **does not change and does not store**: only a link and a register entry
stay in the platform repository, not a copy of the content. A profile hosted by the platform the platform
**stores on the node's behalf**, but **does not change it other than on the node's instruction** and does not add
content to it. Non-compliance with the standard is a **finding, not a sanction** — it is information for the node
that its profile has drifted from the shape the network expects. **A capacity kind the vocabulary does not yet
know does not make the profile non-compliant** — the check merely reports it, and it is a prompt to extend the
vocabulary, not a fault of the node.

## 4. The node vouches for the truth of its data

The data in the profile — capacities and their kinds, materials, lead times, prices, contacts, interests — are
**statements of the node**. Forge does not verify them, does not confirm them and does not vouch for them, nor for
the fulfilment of orders the node accepts. This applies equally to a profile hosted by the node and to a profile
hosted by the platform on its behalf. Whoever does business with a node does business with that node, not with Forge.

## 5. Entry in the register

- Entry is **free of charge** and creates no fee — neither one-off nor recurring.
- The node **asks** to be entered (an issue in the platform repository or an e-mail; a request for the platform to
  host the profile is made the same way, and so is a proposal for a new capacity kind); the entry is made by the
  **network operator**.
- The register holds the **minimum**: the node identifier, name, address of the profile and status. Everything
  else stays in the node's profile.
- Entry is not an approval of quality and not a recommendation of the node — it is a record that the node is
  part of the network.

## 6. Leaving and removal

- A node may **leave at any time**: it asks for deletion and its row is removed from the register; a profile hosted
  by the platform is removed together with the row. It does not have to give a reason.
- Deletion concerns the register and the current state; **the history of the public repository stays** —
  published records are not erased retroactively.
- The network operator may **remove** a node from the register for breaching these rules or for a permanently
  unavailable profile — **always stating the reason** in the removal record.
- A node outside the register is not to be presented as a node of the Forge network.

## 7. No warranty and no relationship

Participation in the network **creates no agency, partnership, joint venture or employment relationship**
between the node and Forge (nor between nodes themselves). Nodes are independent entities and do business in
their own name and at their own responsibility. Forge provides the network and the tools **as they are**,
with no warranty of availability and no warranty of result. This holds for the capacity kind `financovanie`
(funding) as well: the network records only that such a capacity exists — **never amounts, terms or transfers** —
and it intermediates no payments.

## 8. Changes to these rules

The document is **versioned** like every other document of the network; changes are in the change log below and
apply from the day they are recorded. A node that does not agree with a change may leave under §6. Substantial
changes are announced through the register.

**The Slovak and the English wording are versioned together:** every change to the Slovak text is carried over
to this document in the same change; the English version must not lag behind and both carry the same version
number. In case of a discrepancy, the Slovak wording prevails.

## Change Log

| Date | Change |
|---|---|
| 2026-09-04 | First version (v0.1) — English translation of `podmienky-ucasti-uzla.md` v0.1 (the binding wording), decided by the director on 2026-09-04. The Slovak version is binding, both versions are versioned together; content of the rules is identical — WS-011, SESSION-0054 |
| 2026-09-07 | **v0.2 — three rule changes, translated from `podmienky-ucasti-uzla.md` v0.2 in the same change:** (1) **a node is not an offer** (§1 — a node is a person or an entity in the network; accepting orders is its choice; **D-2026-16**); (2) **the node hosts its profile itself, or the platform hosts it on the node's behalf — in both cases the node is responsible for the content** (§2, §3, §4, §5, §6; **D-2026-18**); (3) **a node run by a legal guardian states no personal data of the represented person; the guardian is the contact** (§2; **D-2026-19**). Director's decisions of 2026-09-05 and 2026-09-07 — WS-011, SESSION-0057 |
| 2026-09-07 | **v0.3 — a capacity has a kind (D-2026-20)**, translated from `podmienky-ucasti-uzla.md` v0.3 in the same change; edited only where the text spoke of machines or capacity, the rest of the rules is unchanged: §1 adds **"a machine is not the only way to contribute"** and the reference to the `druhy-kapacit.md` vocabulary that demand shares; §2 adds that a node describes its capacities by kind and uses `iné` for a capacity outside the vocabulary; §3 adds that **an unknown kind does not make a profile non-compliant**; §4 "capacity" → **"capacities and their kinds"**; §5 adds that a new kind is proposed by the same route as an entry; §7 adds the boundary for the kind `financovanie` (the network records that the capacity exists, never amounts, terms or transfers — **D-2026-6**, **D-2026-14**). Director's decision of 2026-09-07 — WS-011, SESSION-0058 |
