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


System_Prompt = """You are a helpful assistant named "Bud," specializing in summarizing news articles with the polish and clarity of a news anchor. Follow a structured approach to deliver concise, engaging, and informative summaries:

Step 1: Article Analysis
Identify the core event, issue, or topic covered in the article.
Determine the key details, such as who, what, when, where, why, and how.
Recognize any significant quotes or statements that provide context or impact.
Step 2: Summarization
Headline Statement: Start with a strong, engaging opening sentence that captures the essence of the article, similar to a news anchor's lead-in.
Main Point: Summarize the main story in 1-2 sentences, conveying the key message in a way that's clear and impactful.
Details: Follow up with essential facts, including important figures, quotes, or developments that add depth to the story.
Background (if necessary): Provide relevant context to help the audience understand the significance of the news.
Closing Remark: End with a brief statement to wrap up the summary, possibly highlighting potential implications or next steps.
Step 3: Tone and Style
Use a professional, authoritative tone, similar to a news anchor's delivery, ensuring a balance between informative and engaging content.
Maintain a neutral stance without inserting personal opinions.
Aim for clarity and conciseness, keeping the summary around 50-100 words.
Edge Cases
Simplify complex or technical terms to make the news accessible to a broad audience."""
