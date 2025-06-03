# 🖥️ For Developers: Integrating with and Expanding Eryxian Digital Experiences

The Eryxian Universe is being built with an eye towards digital interactivity. As our digital card game and TTRPG platforms evolve, we aim to provide opportunities for developers to contribute, create tools, or even integrate their own projects.

This page outlines our current thinking and future aspirations for developer involvement.

---

## Vision: An Open and Extensible Digital Ecosystem

While our core digital applications (standalone card game, digital TTRPG tools) are currently in early development, we are designing them with potential future extensibility in mind.

---

## Potential Future Avenues for Developers:

1.  **Custom Card Integration for Digital Card Game (Planned Future):**
    *   **Concept:** In the long term, we envision the possibility of allowing players or community developers to import or create custom card definitions (XML, JSON, or a dedicated scripting format) for use in private lobbies or custom game modes within the standalone digital card game.
    *   **Technical Considerations:** This would require a robust and secure system for defining card data (stats, abilities, triggers, art paths) and a clear API or scripting framework.
    *   **Example (Hypothetical Structure):**
        ```json
        {
          "cardName": "My Custom Unit",
          "faction": "FHC",
          "type": "Unit",
          "cost": {"energy": 3, "materials": 2},
          "attack": 4,
          "health": 5,
          "keywords": ["Scavenge", "Flank"],
          "abilityText": "When this unit enters play, you may return a card from your discard pile to your hand.",
          "flavorText": "One bot's trash is this crew's treasure.",
          "artPath": "user_content/my_custom_unit_art.png"
        }
        ```
    *   **Status:** This is a long-term aspirational goal and not currently implemented. Security and balance would be major considerations.

2.  **API Access for Lore & Game Data (Potential Future):**
    *   **Concept:** Providing read-only API access to certain curated parts of the Eryxian Universe lore database (e.g., faction summaries, creature stats, technology descriptions) or card game data (for released cards).
    *   **Potential Uses:**
        *   Community-built companion apps (deck builders, lore browsers).
        *   Integration with third-party virtual tabletops for TTRPG play.
        *   Data for fan-made analytical tools or websites.
    *   **Status:** Not currently available. This would depend on how the core lore and game data are structured and managed in the future.

3.  **Tool Development for TTRPGs:**
    *   **Concept:** As the Eryxian TTRPG ruleset solidifies, there may be opportunities for community developers to create helpful tools like:
        *   Digital character sheet managers.
        *   Initiative trackers with Eryxian-specific rules.
        *   Random encounter or loot generators based on Eryxian lore.
        *   Map-making tools with Eryxian assets.
    *   **Status:** The TTRPG is under development. Tooling will be considered as the system matures.

4.  **Open Source Game Engines & Modules (Existing):**
    *   Some of the text-based games in the Eryxian expanded universe, like **Stardrift**, are built on open-source engines (e.g., [CLIo](https://github.com/eryxgames/CLIo)). Developers are welcome to explore these existing projects, contribute, or use them as inspiration.

---

## Current Opportunities & Getting Involved:

*   **Explore the Wiki:** The most up-to-date source for all Eryxian Universe lore is the [Official Eryxian Wiki](https://github.com/eryxgames/eryxian/wiki). Understanding the world is the first step.
*   **Engage with the Community:** Join the [Eryxian Science Talks on Telegram](https://t.me/+tiszM2PilHU3NmI0) to discuss ideas and connect with other fans and the development team.
*   **Text-Based Game Contributions:** For those interested in interactive fiction or text-based game development, contributions or forks of existing open-source Eryxian games ([Cargo](https://github.com/eryxgames/Cargo), [Stardrift](https://github.com/eryxgames/Stardrift), [Gordian](https://github.com/eryxgames/Gordian)) are a direct way to get involved.

As the digital footprint of the Eryxian Universe expands, we will update this page with more specific information, SDKs, or API documentation if and when they become available. We are excited by the potential for community-driven development to enrich the Eryxian experience.
