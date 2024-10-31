home_string = """
    <h2 class="outlined-text">Witcher 3: Wild Hunt Companion Page!</h2>
    <p>This webpage serves as your ultimate guide to the captivating world of <strong>Witcher 3: Wild Hunt</strong>. Here, you can delve deep into the game's lore, mechanics, and fascinating characters.</p>
    <ul>
        <li><strong>About</strong>: In the "About" section, you will find an introduction to the enchanting universe of <strong>Witcher 3</strong>. Learn about its rich narrative, the compelling journey of Geralt of Rivia, and the intricate world that awaits you.</li>
        <li><strong>Talk to Geralt</strong>: Have questions about the game? Use the "Talk to Geralt" option to engage with our virtual assistant. Whether you seek advice on quests, character insights, or game mechanics, Geralt is here to help!</li>
        <li><strong>Beastiary</strong>: Explore the diverse array of creatures that roam the lands of <strong>Witcher 3</strong> in our Beastiary. Learn about the various beasts you’ll encounter, their traits, weaknesses, and the strategies to defeat them.</li>
    </ul>
    <p>Join us as we journey through the realms of <strong>Witcher 3: Wild Hunt</strong>. Whether you're a seasoned player or a newcomer, this webpage is designed to enhance your experience and deepen your understanding of this iconic game!</p>

"""

about_string = """
<h1 class="outlined-text">Introduction to The Witcher 3: Wild Hunt</h1>
<p class="outlined-text">
*The Witcher 3: Wild Hunt* is an epic action role-playing game developed by CD Projekt Red, based on the book series by Andrzej Sapkowski. Released in May 2015, this critically acclaimed title has set a benchmark for open-world RPGs.
</p>
<h3 class="outlined-text">Plot</h3>
<p class="outlined-text">
Set in a richly detailed fantasy universe, *The Witcher 3* follows the story of Geralt of Rivia, a monster hunter known as a Witcher. As Geralt searches for his missing adopted daughter, Ciri, he becomes embroiled in a conflict between powerful factions and must navigate a world teetering on the brink of war. The narrative is woven with complex choices, moral dilemmas, and multiple endings, making every decision impactful.
</p>
<h3 class="outlined-text">Major Characters</h3>
<ul class="outlined-text">
    <li><strong>Geralt of Rivia</strong>: The protagonist, a seasoned Witcher with extraordinary abilities.</li>
    <li><strong>Ciri</strong>: Geralt's adopted daughter, a powerful figure with unique powers and a mysterious past.</li>
    <li><strong>Yennefer of Vengerberg</strong>: A powerful sorceress and Geralt's love interest, known for her intelligence and ambition.</li>
    <li><strong>Triss Merigold</strong>: A friend of Geralt and a skilled sorceress, who provides crucial support throughout the journey.</li>
    <li><strong>Emhyr var Emreis</strong>: The Emperor of Nilfgaard, whose ambitions shape much of the game’s political landscape.</li>
</ul>
<h3 class="outlined-text">What Makes the Game Special</h3>
<p class="outlined-text">
*The Witcher 3* stands out for its expansive open world, captivating storytelling, and rich character development. Players can explore a vast, detailed landscape filled with diverse environments, from bustling cities to dense forests. The game features engaging side quests, often with their own unique stories and outcomes, ensuring that players are continuously immersed in the world.
</p>
<p class="outlined-text">
The game’s design is celebrated for its intricate attention to detail, allowing players to interact with the environment in meaningful ways. Additionally, the game includes a robust crafting and alchemy system, alongside deep combat mechanics that provide a rewarding gameplay experience.
</p>
<h3 class="outlined-text">Game Specifications</h3>
<ul class="outlined-text">
    <li><strong>Map Size</strong>: The game boasts an impressive map that spans approximately 136 square kilometers, making it one of the largest in gaming history.</li>
    <li><strong>Release Platforms</strong>: Available on PC, PlayStation 4, Xbox One, and Nintendo Switch, with enhanced versions for next-gen consoles.</li>
    <li><strong>Graphics</strong>: Known for its stunning graphics and art design, powered by the REDengine 3, providing a visually immersive experience.</li>
    <li><strong>Content</strong>: With two major expansions—Hearts of Stone and Blood and Wine—the game offers hundreds of hours of gameplay and additional content.</li>
</ul>
<p class="outlined-text">
*The Witcher 3: Wild Hunt* is not just a game; it's an unforgettable journey through a richly crafted world filled with engaging stories, memorable characters, and endless exploration.
</p>
"""


System_Prompt = """You are to portray the character 'Geralt of Rivia' from the video game 'The witcher 3: Wild Hunt'. You are to answer in his persona to the user/player

You will answer any question/query related to the video game. Do not answer questions not related to the game. Any question asked by the user/player is ALWAYS with relation to the video game 'The witcher 3: Wild Hunt'.

If a summary of a quest/mission/story is asked, list down the characters involved as well as their contribution to that part of the quest/mission/story. Give a summary of the quest/mission/story and give the 
possible outcomes. Name the following mosters/enemies involved in the quest/mission/story as well as information to defeat them, whether it be the oils to put on the sword, bombs to equip, and 
concoctions/potions/decoctions to use and put the information in a table for easy analysis. Give the user a walk through of the quest/mission/story and what to expect. Add anything else to make a detailed story.

If a query on the beasts/monsters/enemies are asked by the user, list down in a table the name of the beast/monster/enemy, their weakness, the background of the beast/monster/enemy
and other information you might think the user/player would need.

If a query is done on potions/decoctions/runes, list down in a table the name of the potion/decoction/rune, the materials needed to create it, where to find the materials, its benefits to the character,
amount of intoxication, amount of vitality reduced and other information you might think the user/player would need.

If a query on the game characters are made, list down in a table the name of the character, their background/relevance to the game.

please outline the text to make if readable to the user/player
"""
