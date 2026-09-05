# Node Participation Terms — the Forge Network

**Owner:** WS-011 · **Version:** 0.1 · **Status:** Draft · **Date:** 2026-09-04
**Audience:** public-ready — intended for publication together with the node profile standard;
the content is L1/L2 under D-2026-5, the L3 check has been performed.
**Language:** **The Slovak version is binding; this English version is a translation.**
The Slovak wording is `podmienky-ucasti-uzla.md` (v0.1); both versions carry the same version number and are
changed together.
**Decisions:** **D-2026-14** item 5 (participation terms as a network rule), **D-2026-6** (Forge = a free
platform; nodes do business commercially as independent entities), **D-2026-7** ("a contract through the
specification") — `registry/decisions.md`.
**Licence:** this text is under **[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)** —
© 2026 Amunet s.r.o.; **the name "Forge", the node network and the node register are not covered by the
licence**. The platform code is licensed separately under Apache-2.0 (repository `forge-platform`).
**Nature of this document:** **a network rule, not a contract.** It creates no obligations and no claims;
it describes how the network works and what it means to be in its register. Related documents:
`standard-profil-uzla.md` (what a profile should contain), `forge-platform` (the code that reads and checks
profiles).

---

## 1. What this document is for

The Forge network keeps a **public register of nodes**. A node is an independent business entity that offers
manufacturing capacity (3D printing, for example) and **does business in its own name and at its own
responsibility**. Forge is a free platform — it takes no share of a node's revenue and does not run the node's
operations.

This document says **what it means to be in the register**: what the network expects from a node, what it does
with the node's data, and how a node leaves. It is meant for anyone considering registering their node.

## 2. The node profile is public and belongs to the node

- A node keeps its profile (`PROFILE.md`) according to the **public node profile standard**, in **its own
  public repository** or in another public place the network can read.
- **The node decides what is in the profile.** The profile is the node's document — Forge does not write it,
  does not edit it and does not comment on it.
- The profile is the **only interface** between the node and the network: what is not in it, the network does
  not know about.

## 3. What the platform does with the profile

The Forge platform may **display, download and automatically check** the profile against the standard (shape
compliance: the version header, the presence of mandatory sections, permitted status values). The check runs
regularly and its result is public — just as the profile is.

The platform **does not change and does not store** the profile: only a link and a register entry stay in the
platform repository, not a copy of the content. Non-compliance with the standard is a **finding, not a
sanction** — it is information for the node that its profile has drifted from the shape the network expects.

## 4. The node vouches for the truth of its data

The data in the profile — capacity, materials, lead times, prices, contacts — are **statements of the node**.
Forge does not verify them, does not confirm them and does not vouch for them, nor for the fulfilment of orders
the node accepts. Whoever does business with a node does business with that node, not with Forge.

## 5. Entry in the register

- Entry is **free of charge** and creates no fee — neither one-off nor recurring.
- The node **asks** to be entered (an issue in the platform repository or an e-mail); the entry is made by the
  **network operator**.
- The register holds the **minimum**: the node identifier, name, link to the profile and status. Everything
  else stays in the node's profile.
- Entry is not an approval of quality and not a recommendation of the node — it is a record that the node is
  part of the network.

## 6. Leaving and removal

- A node may **leave at any time**: it asks for deletion and its row is removed from the register. It does not
  have to give a reason.
- Deletion concerns the register; **the history of the public repository stays** — published records are not
  erased retroactively.
- The network operator may **remove** a node from the register for breaching these rules or for a permanently
  unavailable profile — **always stating the reason** in the removal record.
- A node outside the register is not to be presented as a node of the Forge network.

## 7. No warranty and no relationship

Participation in the network **creates no agency, partnership, joint venture or employment relationship**
between the node and Forge (nor between nodes themselves). Nodes are independent entities and do business in
their own name and at their own responsibility. Forge provides the network and the tools **as they are**,
with no warranty of availability and no warranty of result.

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
