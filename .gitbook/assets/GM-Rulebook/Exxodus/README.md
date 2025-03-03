# Exxodus: Limited Edition - Game Rules (v1.1e)
(Predecessor of Eryxian games)
---
Created by Daniel Sandner
---
This document outlines the rules for Exxodus: Limited Edition, a strategic card game of interstellar trade, combat, and corporate stellar conquest and dominance.

## Table of Contents

1.  [Overview](#overview)
2.  [Game Components](#game-components)
3.  [Setup](#setup)
4.  [Gameplay](#gameplay)
    *   [Player Turns](#player-turns)
    *   [Actions](#actions)
    *   [Placing Cards](#placing-cards)
    *   [Card Stacks](#card-stacks)
    *   [Trading (Economics)](#trading-economics)
    *   [Combat (Fight)](#combat-fight)
        *   [Fleet Combat](#fleet-combat)
        *   [Planet Assault](#planet-assault)
        *   [Leader Duels](#leader-duels)
5.  [Card Types](#card-types)
    *   [Planets](#planets)
    *   [Ships](#ships)
    *   [Leaders](#leaders)
    *   [Technology (Tech)](#technology-tech)
    *   [Missions](#missions)
6.  [Card Anatomy](#card-anatomy)
7.  [Winning the Game](#winning-the-game)
8.  [Tournament Modifications](#tournament-modifications)
9.  [Frequently Asked Questions (FAQ)](#frequently-asked-questions-faq)
10. [Credits](#credits)

## 1. Overview <a name="overview"></a>

Exxodus is a card game where players compete to accumulate Value Points (VP) through controlling planets, establishing trade routes, building fleets, and engaging in combat.  The game combines strategic resource management with tactical card play.

## 2. Game Components <a name="game-components"></a>

*   A single, shared deck of cards (referred to as the "RESOURCES" deck). This deck contains all card types.
*   Credit tokens (used for purchasing cards and other actions).

## 3. Setup <a name="setup"></a>

1.  Shuffle the RESOURCES deck thoroughly.
2.  Deal each player 5 cards from the RESOURCES deck.
3.  Give each player 5 credit tokens.

## 4. Gameplay <a name="gameplay"></a>

### 4.1 Player Turns <a name="player-turns"></a>

Players take turns in clockwise order.  At the *beginning* of each player's turn, they draw one card from the RESOURCES deck.

### 4.2 Actions <a name="actions"></a>

A player can perform up to **three actions** during their turn.  The available actions are:

*   **Play a Card:**  Place a card from your hand into play (see [Placing Cards](#placing-cards)).  This costs 1 action + the card's credit cost (its "VALUE").
*   **Trade:**  Establish a trade route between two planets (see [Trading](#trading-economics)).  This costs a variable number of actions, depending on the number of ships in the Merchant Fleet.
*   **Attack:** Initiate combat with an opponent's fleet, planet, or Leader (see [Combat](#combat-fight)). This costs a variable number of actions.
*   **Move a Ship/Leader:** Move a Ship or Leader card between stacks. This costs 1 Action + the card's VALUE in credits.

**Important Action Notes:**

*   A player can only perform the **Trade** action *once* per turn.
*   Other actions (Play a Card, Attack, Move a Ship/Leader) can be performed multiple times, as long as the player has enough actions remaining. For example, a player could attack three times, or play three cards, or attack twice and play one card.

### 4.3 Placing Cards <a name="placing-cards"></a>

To play a card, a player must:

1.  Spend one action.
2.  Pay the card's credit cost (its "VALUE"), unless special rules on the card state otherwise.

Cards can be played in one of two ways:

*   **Individually:**  The card is placed on the table as a separate entity (e.g., a Corporate Resource).
*   **Into a Stack:** The card is added to an existing stack of cards (see [Card Stacks](#card-stacks)).

### 4.4 Card Stacks <a name="card-stacks"></a>

*   Cards of certain types can be stacked together.  When cards are stacked, their statistics (Power, Shield, TECH, etc.) are added together.
*   Ships and Leaders can move *between* existing stacks.  This costs 1 action and the card's credit value, similar to playing the card from your hand.
*    "Double" cards statistics affect the game with the numbers that correspond to the card's owner.
*   Stacks involving ships are often referred to as "Wings" or "Fleets." A Wing can contain a maximum of 3 ship cards.

### 4.5 Trading (Economics) <a name="trading-economics"></a>

Trading allows players to generate credits by transporting commodities between planets.

**Requirements for Trade:**

1.  **Merchant Fleet:** The player must have at least one Ship card (forming a Merchant Fleet) on the *origin* planet (the planet the goods are coming *from*).
2.  **Tradable Commodity:** The origin planet must have a value *greater than 0* for the commodity being traded.
3. **Two Planets**: Trade must be performed between two planets.

**Trade Process:**

1.  **Action Cost:** The number of actions required for a trade is equal to the number of Ship cards in the Merchant Fleet on the origin planet (up to a maximum of 3 actions for 3 ships).
2.  **Revenue Calculation:**
    *   Determine the value of the commodity being traded on the *origin* planet.
    *   Subtract any Docking Fees (paid to the owner of the *destination* planet). The Docking Fee is typically the POP level of the destination planet.
    *   Subtract any other modifiers.
    *   The result is the player's profit in credits.

**Example:**

A player wants to trade POP (Population) from Procyon (POP value of 4) to Helios (POP value of 1, and thus a Docking Fee of 1).  They have one ship on Procyon.

*   Action Cost: 1 action (because there's one ship).
*   Revenue: 4 (Procyon POP) - 1 (Helios Docking Fee) = 3 credits.
*   If any other special rules apply that affect trade, those are also included. For example 4-1-1=2

### 4.6 Combat (Fight) <a name="combat-fight"></a>

Combat occurs when a player chooses to attack an opponent's fleet, planet, or Leader.

**Phases of Combat:**

1.  **Declaration of Fight:** The attacking player declares which of their Wings/Fleets (or single Leader card) is attacking, and what they are attacking. Only one Wing/Fleet per side can participate in a single fight.
2.  **Calculation of Fight:**
    *   **Power:** The attacking force's total Power is calculated (summing the Power of all cards in the stack, plus any modifiers).
    *   **Shield/Defense:** The defending force's total Shield (for fleets) or Defense (for planets) is calculated.
    *   **Success:** If the attacking Power is greater than or equal to the defending Shield/Defense, the attack is successful.
3.  **Fight Result:** Determine damage and remove cards from the game.

#### 4.6.1 Fleet Combat <a name="fleet-combat"></a>

*   **Speed:**  The Speed stat determines the order of attacks.  A fleet with a higher Speed attacks *before* a fleet with a lower Speed.  If a faster fleet inflicts enough damage to destroy or damage the slower fleet, the slower fleet may not get to attack at all.
*   **Damaged Ships:** Ships that are damaged in combat *cannot attack*.  A damaged ship is marked (rotated, with a token, etc.).
*   **Wing/Fleet Speed:** The Speed of a Wing/Fleet is determined by the *slowest* ship in the Wing.
* **Number of Ships in Wing:** Determines the time cost of an attack. 2 Ships cost 2 actions, 3 ships cost 3 actions.
*   **Repairing Ships:** Damaged ships can be repaired by moving them to a planet *controlled by the player*.  This costs actions and credits, just like moving a ship normally.
*   Ships/fleets with a speed of 0 or less CAN NOT attack!

#### 4.6.2 Planet Assault <a name="planet-assault"></a>

*   Planet assaults are resolved similarly to fleet combat.
*   The planet's TECH level is its base attack value.
*   All cards stacked on the planet (including any active Missions or Tech cards) contribute their stats to the planet's defense.
*   If the attack is successful and "damages" the planet, the *defending player* chooses which upgrades (stacked cards) to discard.
*   If a planet has *no* upgrades remaining and is successfully attacked, ownership of the planet card changes to the attacker.

#### 4.6.3 Leader Duels <a name="leader-duels"></a>

*   Only a Leader card played *individually* (not as part of a stack) can initiate a Leader duel.  This is considered an "assassination" attempt.
*   A Leader duel costs 3 actions (the attacking player's entire turn).
*   In a Leader duel, *all* stats of both Leaders (including any modifiers affecting the game) are added up.
*   The Leader with the higher total wins the duel. The losing Leader card is removed from the game.
*   If the totals are equal, *both* Leader cards are removed from the game.

## 5. Card Types <a name="card-types"></a>

### 5.1 Planets <a name="planets"></a>

*   Represent planetary resources and defenses.
*   Key statistics:
    *   **TECH:**  Used for technological advancements and defense.
    *   **DEF:**  Defensive strength against attacks.
    *   **POP:**  Represents population and is used for certain trade routes.
*   Planet cards often have special abilities or modifiers (e.g., Docking modifiers).

### 5.2 Ships <a name="ships"></a>

*   Used for both trade (Merchant Fleets) and combat (Military Fleets).
*   Key statistics:
    *   **Power:** Attack strength.
    *   **Shield:** Defensive strength.
    *   **Speed:** Determines attack order in combat.
*   Ships can be moved between stacks (at a cost).

### 5.3 Leaders <a name="leaders"></a>

*   Can act as fleet commanders, planetary governors, or corporate leaders.
*   When stacked with ships or on a planet, their statistics influence the entire stack.
*   Only Leaders played *individually* can initiate Leader duels.

### 5.4 Technology (Tech) <a name="technology-tech"></a>

*   Represent technological advancements.
*   Can be played as individual projects or added to stacks to improve them.
*   **Breakthrough (Experimental Technology):** Tech cards can be played *anytime* (even during combat or another player's turn) for a cost of VALUE x2.  In this case, the Tech card only remains in play until the end of the current action.

### 5.5 Missions <a name="missions"></a>

*   Represent secret agendas and special operations.
*   Can be played during the player's turn for 1 action + VALUE.
*   Can be played *anytime* (even during combat or another player's turn) for a cost of VALUE.  In this case, the Mission card only remains in play until the end of the current action.
*   Missions can be played on *any* card in play, regardless of owner.

## 6. Card Anatomy <a name="card-anatomy"></a>

A typical Exxodus card has the following elements:

*   **Card Type:** (Planet, Ship, Leader, Tech, Mission) -  Indicated by an icon.
*   **Card Name:** The name of the specific card.
*   **Statistics:** Numerical values representing the card's attributes (e.g., Power, Shield, TECH, DEF, POP). These vary depending on the card type.
*   **Special Ability (Upgrade Special):**  A text box describing any special abilities the card has.  These abilities may be active even when the card is in a stack.
*   **VALUE:** The card's credit cost. This is the amount of credits needed to play the card.
*   **Special Card Ability/Properties:** Special abilities that are active only when the card is *not* in a stack (for Leaders, Ships, etc.). For Planets, this usually indicates Docking rules or other modifiers.

    * Some cards may be noted as an "ALIEN RESOURCE". These cards do *not* cost credits to play, but also do *not* add any VALUE to the final score.

## 7. Winning the Game <a name="winning-the-game"></a>

The game ends when one of the following conditions is met:

1.  **Empty RESOURCES Deck:**  The RESOURCES deck is empty, and the last player finishes their turn.
2.  **Target Card Value:** A player reaches a combined VALUE of cards on their table (in play) of a predetermined amount (recommended 25).
3.  **Target Credit Value:** A player reaches a predetermined amount of credits (recommended 25).

The winner is the player with the *most* Value Points (VP) at the end of the game.  VP are calculated as follows:

*   **Card Value:**  Sum the VALUE of all cards the player has in play.
*   **Credits:**  Every 5 credits remaining counts as 1 VP.

*You cannot trade cards for credits after the game ends.*

## 8. Tournament Modifications <a name="tournament-modifications"></a>

These optional rules can be used to modify gameplay, especially for tournament play.  They can be combined.

*   **Assault:** Destroyed ships return to the owner's hand.
*   **Cyberfusion:**  All stats of a WING, *including SPEED*, are added together. If a WING is damaged, *all* ships in the WING are damaged (or destroyed).
*   **Conquest:** Only the values of planets in play count towards the final score.
*   **Grant:** At the beginning of their turn, a player replenishes their hand from the RESOURCES deck to have at least 5 cards.
*   **Revolution:** Damaged ships *can* attack.

## 9. Frequently Asked Questions (FAQ) <a name="frequently-asked-questions-faq"></a>

*   **Q: What does "winning a battle" mean for Commander Buck Firewall (a Leader card)?**
    *   A: It means removing an opponent's card from the game as a result of combat (destroying an enemy ship or a planetary upgrade).

*   **Q: When is an economic bonus (like on the Cargo Liner ship) applicable?**
    *   A: Whenever the card's *owner* is performing the Trade action during *their* turn.

*   **Q: What is a "Modification (MOD)"?**
    *   A: Modification cards are TECHNOLOGY (Tech) and MISSION cards.  Some cards (like the ELDERAN planet) are immune to their effects.

*   **Q: When can I use Special Card Abilities?**
    *   A: Special abilities can be used at *any time* during the game, including during your opponent's turn, as long as the ability's text allows it.  For example, a Star Fighter ship might use its ability to damage an enemy ship whenever it's most strategically advantageous. Fights are resolved *after* all modifiers are calculated.

*   **Q: What happens if multiple players play effect cards simultaneously?**
    *   A: The player whose turn it is resolves their card effects first.  If it's neither player's turn, all simultaneously played cards are removed from the game (this is the "Time Paradox Rule").

*   **Q: Who benefits from the VALUE of a Mission card played against an opponent?**
    *   A: The player who *has the card on their table* (their "corporation") benefits from the VALUE, regardless of who originally owned the Mission card.

*    **Q: What happens with Card-duplicates (f.i. Mission - UPLINK), if source of copy leaves the game?**
    * A: It is removed from the game too.

*   **Q: When to play Mission - Winds of War?**
    *   A: You shall play this card if the situation in the game means a lost battle (losing a ship or planetary upgrade). However, an opponent can play other game modificators afterward (this means, Winds of War does not mean an ultimate situation win).

*   **Q: Is it possible to trade (with technologies) on a planet with basic TECH 1, when there is a modification card in effect (f.i. TECHNOLOGY), which globally lowers TECH - 1 on the target player table?**
    *   A: If the statistics of the target commodity is, after adding/subtracting all modifiers, 0 or lower, you cannot use that trade route on the planet.

*   **Q: How does the XTECH modifier work with cards like Leader - OR-SLAGG THE WARRIOR?**
    *   A: OR-SLAGG does not use "advanced" technologies. Technology cards have no effect on him or any stack he is in. However, his opponents *can* benefit from any TECH that is applied to them.

## 10. Credits <a name="credits"></a>

*   Game Design: Daniel Sandner
*   Publisher: DarkFusion Studios

Enjoy the game!



Formatted list of the Exxodus cards from the images, including their stats and descriptions. Organized  by type (Planet, Leader, Ship, Tech, Mission) 

**Note:** I am using the following abbreviations for card statistics:

*   **TECH:** Technology
*   **DEF:** Defense
*   **POP:** Population
*   **VALUE:** Credit Cost
*   **CHAR:** Charisma
*   **LEAD** Leadership
*   **AGILITY** Agility
*   **POWER:** Ship Attack Power
*   **SHIELD:** Ship Defense Shield
*   **SPEED:** Ship Speed


## Exxodus Card List

### Planets

1.  **HELIOS**
    *   Type: Planet
    *   TECH: 0
    *   DEF: +1
    *   POP: -1
    *   VALUE: 1
    *   Special: SPECIAL: Trading bonus.

2.  **CASSIUS**
    *   Type: Planet
    *   TECH: +1
    *   DEF: -1
    *   POP: +1
    *   VALUE: 1

3.  **TITANIA**
    *   Type: Planet
    *   TECH: +1
    *   DEF: 0
    *   POP: +2
    *   VALUE: 1
    *   Special: UPGRADE FANATICS: All modifications played on this planet are 1 credit cheaper.

4.  **HERMES IV**
    *   Type: Planet
    *   TECH: -1
    *   DEF: 0
    *   POP: +1
    *   VALUE: 1
    *   Special: TOURIST ROUTE: Trading bonus to passenger ship revenues.

5.  **TERRA NOVA**
    *   Type: Planet
    *   TECH: 2
    *   DEF: 2
    *   POP: -2
    *   VALUE: 1
    *   Special: RESERVATION: All technology achievements are ignored.

6.  **ELDERAN**
    *   Type: Planet
    *   TECH: +1
    *   DEF: 2
    *   POP: -2
    *   VALUE: 2
    *   Special: RIGID SOCIETY: Immune to modifications.

7.  **CALEDONIA**
    *   Type: Planet
    *   TECH: 2
    *   DEF: -2
    *   POP: +2
    *   VALUE: 2

8.  **BLACKMOOR**
    *   Type: Planet
    *   TECH: +1
    *   DEF: -1
    *   POP: +2
    *   VALUE: 1

9. **EXXODUS**
    *  Type: Planet
    *   TECH: 2
    *   DEF: 0
    *   POP: -1
    *   VALUE: (Alien Resource - no cost, no value)
    *   Special: DOOMED ALIEN PLANET: Put class-M ship from your resources in game. Destroy Exxodus.

10. **PROCYON**
    *  Type: Planet
    *   TECH: 2
    *   DEF: +1
    *   POP: -2
    *   VALUE: 2
    *   Special: SCRAPMETAL TRADER.

### Leaders

1.  **AEN STARK**
    *   Type: Leader
    *   CHAR: +1
    *   LEAD: -1
    *    AGILITY: -1
    *   VALUE: 1
    *   Special: IMMUNE. Ignores target docking costs.

2.  **OR-SLAGG THE WARRIOR**
    *   Type: Leader
    *   CHAR: -1
    *   LEAD: +2
    *   AGILITY: -2
    *   VALUE: 2
    *   Special: ASSASIN. When fighting enemy leader, his agility is doubled.

3.  **COMMANDER BUCK FIREWALL**
    *   Type: Leader
    *   CHAR: 0
    *   LEAD: +2
    *   AGILITY: -2
    *   VALUE: 2
    *   Special: After winning a battle, draw one card from resources.

4. **HIGH COMMANDER DRAGG VOXX**
      * Type: Leader
    *   CHAR: 0
    *   LEAD: +2
    *   AGILITY: -2
    *   VALUE: 2
    * Special: BATTLE TACTICS. Put one target ship in battle to your resources.

5.  **SWIGG THE PRIVATEER**
    *   Type: Leader
    *   CHAR: +1
    *   LEAD: -1
    *   AGILITY: +2
    *   VALUE: 1
    *   Special: Steal 1 credit from target trade revenue.

6.  **DOC BRAINAC**
    *   Type: Leader
    *   CHAR: -1
    *   LEAD: +1
    *   AGILITY: 0
    *   VALUE: 1
    *   Special: RESEARCHER: Experiment costs are halved.

### Ships
(duplicated cards are listed only once, with stats)

1.  **CARGO LINER** (M-CLASS)
    *   Type: Ship
    *   POWER: +1
    *   SHIELD: 0
    *   SPEED: +1
    *   VALUE: 1
    *   Special: CARGO ROUTE: Trading bonus to goods trade revenues.

2.  **RAPTOR** (S-CLASS)
    *   Type: Ship
    *   POWER: +1
    *   SHIELD: -1
    *   SPEED: +1
    *   VALUE: 1

3.  **STAR FIGHTER** (S-CLASS)
    *   Type: Ship
    *   POWER: +1
    *   SHIELD: 0
    *   SPEED: +2
    *   VALUE: 2
    *   Special: Damage target ship. Destroy ship STAR FIGHTER.

4.  **FRIGATE** (M-CLASS)
    *   Type: Ship
    *   POWER: +1
    *   SHIELD: -1
    *   SPEED: +2
    *   VALUE: 1

5.  **DESTROYER** (L-CLASS)
    *   Type: Ship
    *   POWER: +2
    *   SHIELD: -2
    *   SPEED: -1
    *   VALUE: 3

6.  **RAIDER** (S-CLASS)
    *   Type: Ship
    *   POWER: +2
    *   SHIELD: 0
    *   SPEED: -1
    *   VALUE: 2
    *   Special: Destroy target technology. Destroy ship RAIDER.

7.  **CRUISER** (M-CLASS)
      *   Type: Ship
    *   POWER: +2
    *   SHIELD: 0
    *   SPEED: -1
    *   VALUE: 2

8.  **STINGER** (M-CLASS)
    *   Type: Ship
    *   POWER: +2
    *   SHIELD: -1
    *   SPEED: +1
    *   VALUE: 1

### Tech

1.  **CYBERSYMBIONTS**
    *   Type: Tech
    *   +1 / +1 / -1
    *   VALUE: 2
    *   Special: -1 credit: REPULSIVE APPEARANCE: Trading penalty to all trade revenues.

2.  **PROSPECTIVE MATERIALS**
    *   Type: Tech
    *   +1 / +0 / +1
    *   VALUE: 2
    *   Special: +1: GALACTIC PATENT: Trading bonus to goods trade revenues.

3.  **MOLECULAR DISINTEGRATOR**
    *   Type: Tech
    *   +1 / +1 / -1
    *   VALUE: 2
    *   Special: TEMPORARY POWER BOOST: If you pay additional 2 credits in battle, card bonus is doubled.

4.  **FOCUSED EXPERIMENTS**
    *   Type: Tech
    *    +1/+1/-2
    *   VALUE: 2
    *   Special: CONTINUAL RESEARCH: Experimental technology returns it back to your resources.

5.  **QUANTUM PHASOR** DOUBLE CARD
    *   Type: Tech
    *   +1 / +0 / +1
    *   VALUE: 2
    *   Special: QUANTUM PHASING

    **QUANTUM REACTOR**
    *   Type: Tech
    *   -1 / +2 / -1
    *   VALUE: 2
    *   Special: QUANTUM PHASING    

6. **ENERGY TRACER** DOUBLE CARD
    * Type: Tech
    * +1 / +0 / +1
    * Value: 2
    * Special: POWER COMPRIMATION

   **ENERGY DISPERSION**
    * Type: Tech
    * -2 / +1 / +1
    * Value: 2
    * Special: POWER COMPRIMATION    

7. **BIO AUGMENTATION** DOUBLE CARD
      * Type: Tech
    * +2/+1/-2
    * Value: 2
    * Special: BIO ENHANCEMENT

   **CYBORG PROJECT**
    * Type: Tech
    * -2/+2/+1
    * Value: 2
    * Special: BIO ENHANCEMENT    

8.  **CLOAKING DEVICE** DOUBLE CARD
    *  Type: Tech
    * +1 / +1 / -1
    * Value: 2
    * Special: SPATIAL CONVERSION

   **CONVERSION FIELD**
    *  Type: Tech
    * -1 / +2 / -1
    * Value: 2
    * Special: SPATIAL CONVERSION    

### Missions

1.  **MEGA CORPORATION**
    *   Type: Mission
    *   +1 / +2 / -1
    *   VALUE: 2
    *   Special: CORPORATE POLITICS: Trading bonus to target trade revenues.

2.  **SYSTEM COLLAPSE**
    *   Type: Mission
    *   +1 / +1 / -1
    *   VALUE: 2
    *   Special: POWER SHOTCUT: Destroy target technology. Destroy SYSTEM COLLAPSE.

3.  **DEPRESSION**
    *   Type: Mission
    *   +1 / +2 / -1
    *   VALUE: 2
    *   Special: CORPORATE POLITICS: Trading bonus to target trade revenues.

4.  **UPLINK**
    *   Type: Mission
    *   X / X / X
    *   VALUE: 2
    *   Special: TECH COPY: Exact copy of target technology.

5.  **WINDS OF WAR** DOUBLE CARD
    *   Type: Mission
    *   +2 / 0 / -1
    *   VALUE: 3
    *   Special: You may play this card for free just before losing a battle.

    **WINDS OF WAR** DOUBLE CARD
    *   Type: Mission
    *   +1 / +2 / -2
    *   VALUE: 3
    *   Special: You may play this card for free just before losing a battle.    

6.  **MILITARISTIC REVOLUTION** DOUBLE CARD
    *   Type: Mission
    *   +2 / 0 / -1
    *   VALUE: 1
    *   Special: double card

    **ISOLACIONISTIC REVOLUTION** DOUBLE CARD
    *   Type: Mission
    *   -1 / +2 / -2
    *   VALUE: 1
    *   Special: double card    

7.  **TECHNOCRATIC REVOLUTION** DOUBLE CARD
    *   Type: Mission
    *   +2 / 0 / -1
    *   VALUE: 2
    *   Special: double card

    **FUNDAMENTALISTIC REVOLUTION** DOUBLE CARD
    *   Type: Mission
    *   -1 / -1 / +2
    *   VALUE: 2
    *   Special: double card    

8.  **UNAUTHORIZED ACCESS**
    *   Type: Mission
    *   X / X / X
    *   VALUE: 2
    *   Special: PARTIAL DATA STRUCTURE: Copy of basic statistics of target modification.


This list provides a complete overview of the cards shown in the images, including their stats and special abilities, formatted for clarity and easy reference. This should be helpful for understanding the card interactions and potential strategies in Exxodus.


# Strengths of the Exxodus System:

*   **Interconnected Mechanics:** The core loop of resource gathering (drawing cards), spending resources (credits and actions), trading, and combat is well-integrated. Actions are a limited resource that force meaningful choices.
*   **Asymmetric Card Abilities:** The different card types and their special abilities create asymmetry, leading to diverse strategies. Players aren't just playing "numbers"; they're leveraging unique card interactions.
*   **Stacking Mechanic:** The card stacking system adds a layer of depth. It encourages players to build up powerful fleets or planetary defenses, but also makes those stacks vulnerable. The ability to move Ships and Leaders between stacks adds tactical flexibility.
*   **Variable Game End Conditions:** The multiple win conditions (empty deck, target value, target credits) prevent the game from becoming overly predictable. It allows for different strategic focuses.
*   **Combat Resolution with Speed:** The Speed stat in combat is a good design choice. It creates a "rock-paper-scissors" dynamic and prevents straightforward power comparisons from being the sole determinant of victory.
*   **Trade System Complexity:** The trade system, with its action costs, commodity values, and docking fees, provides a satisfying economic engine without being overly cumbersome.
*    **Theme:** The game combines the elements of space combat and strategy well.

# Weaknesses and Areas for Improvement (Analysis):

*   **Shared Resource Deck:** While simple, a shared resource deck can lead to luck-of-the-draw issues. One player might consistently draw the cards they need, while another struggles.  This reduces player agency. **Use Drafting (Mitigate Luck), allow more cards at beginning, discard over limit and reshuffle resources, and "Scry" Mechanic (preview some cards for a price, maybe later in the game)
*   **Potential for Runaway Leaders:** If a player gets an early lead (e.g., strong planets and trade routes), it might be difficult for others to catch up. The game lacks explicit "catch-up" mechanics.
*   **Complexity in Combat:** While the Speed mechanic is good, the overall combat system (especially with stacked cards, special abilities, and Missions) can become complex to resolve.  The timing rules in the FAQ hint at potential for confusion.
*   **Limited Player Interaction (Potentially):** The game could potentially become somewhat "multiplayer solitaire," where players focus primarily on building their own empires with limited direct interaction, aside from occasional attacks.
*   **Action Economy Tightness:** Three actions per turn *might* feel restrictive, especially in the mid-to-late game when players have more options.  This could slow down the pace.
*   **Double Card Rules** The rule might be confusing for new players.


