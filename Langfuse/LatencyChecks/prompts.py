# prompts = [
#     "Describe the process of photosynthesis.",
#     "What is the capital of France?",
#     "Explain the theory of relativity in simple terms.",
#     "How does quantum computing work?",
#     "What is artificial intelligence?",
#     "Tell me a 100-word story about a detective solving a mystery.",
#     "Explain the concept of blockchain and its uses.",
#     "What are the causes and effects of global warming?",
#     "Describe the life cycle of a butterfly.",
#     "What are the benefits of regular physical exercise?"
# ]

prompts = [

    {"tag":"Data Extraction","content" : """
    Extract the name of places in the following text.
    Desired format:
    Place: <comma_separated_list_of_places>
    Input: "Although these developments are encouraging to researchers, much is still a mystery.
    “We often have a black box between the brain and the effect we see in the periphery,” says Henrique Veiga-Fernandes, a neuroimmunologist at the Champalimaud Centre for the Unknown in Lisbon.
    “If we want to use it in the therapeutic context, we actually need to understand the mechanism.“"
    """
     },

    {"tag":"Text Summarization","content" : """
    Antibiotics are a type of medication used to treat bacterial infections.
    They work by either killing the bacteria or preventing them from reproducing, allowing the body’s immune system to fight off the infection.
    Antibiotics are usually taken orally in the form of pills, capsules, or liquid solutions, or sometimes administered intravenously.
    They are not effective against viral infections, and using them inappropriately can lead to antibiotic resistance.
    Explain the above in one sentence:
    """
     },

    {"tag":"Information Extraction","content" : """
    Author-contribution statements and acknowledgements in research papers should state clearly and specifically whether, and to what extent, the authors used AI technologies such as ChatGPT in the preparation of their manuscript and analysis.
    They should also indicate which LLMs were used. This will alert editors and reviewers to scrutinize manuscripts more carefully for potential biases, inaccuracies and improper source crediting. Likewise, scientific journals should be transparent about their use of LLMs, for example when selecting submitted manuscripts.
    Mention the large language model based product mentioned in the paragraph above:
    """
    },

    {"tag":"Question Answering","content" : """
    Answer the question based on the context below. Keep the answer short and concise. Respond "Unsure about answer" if not sure about the answer.
    Context: Teplizumab traces its roots to a New Jersey drug company called Ortho Pharmaceutical. There, scientists generated an early version of the antibody, dubbed OKT3. Originally sourced from mice, the molecule was able to bind to the surface of T cells and limit their cell-killing potential. In 1986, it was approved to help prevent organ rejection after kidney transplants, making it the first therapeutic antibody allowed for human use.
    Question: What was OKT3 originally sourced from?
    Answer:
    """
    },

    {"tag":"Text classification","content" : """
    Classify the text into neutral, negative or positive.
    Text: I think the food was okay.
    Sentiment:
    """
    },

    {"tag":"Conversation","content" : """
    The following is a conversation with an AI research assistant. The assistant tone is technical and scientific.
    Human: Hello, who are you?
    AI: Greeting! I am an AI research assistant. How can I help you today?
    Human: Can you tell me about the creation of blackholes?
    AI:
    """
    },

    {"tag":"Coding","content" : """
    Table departments, columns = [DepartmentId, DepartmentName]
    Table students, columns = [DepartmentId, StudentId, StudentName]
    Create a MySQL query for all students in the Computer Science Department
    """
    },

    {"tag":"Reasoning","content" : """
    The odd numbers in this group add up to an even number: 15, 32, 5, 13, 82, 7, 1.
    Solve by breaking the problem into steps. First, identify the odd numbers, add them, and indicate whether the result is odd or even.
    """
    },

    {
        "tag":"Advanced Data Extraction", "content": """
    In the field of climate change science, one of the key challenges is understanding the interaction between global warming and regional weather patterns. Over the past century, the Earth's climate has been undergoing significant changes, with rising average global temperatures, shifting weather patterns, and an increase in the frequency and intensity of extreme weather events. Scientists and researchers are constantly working to better understand the underlying causes and consequences of these changes, in order to predict future climate scenarios and mitigate the effects of climate change. This report analyzes the relationship between human-induced greenhouse gas emissions and changes in regional weather patterns, based on a comprehensive study conducted over the past five decades.

    The study examines data from numerous weather stations across the globe, highlighting the increase in global average temperatures and the effect it has had on precipitation patterns, storm occurrences, and the frequency of extreme events like hurricanes, floods, and heatwaves. It explores regional variations in temperature changes, noting how certain areas have seen more drastic temperature increases than others. The report also delves into projections for the future, suggesting that some regions, particularly in tropical and coastal areas, will be more vulnerable to the negative effects of climate change than others.
    
    In particular, the study focuses on the rising sea levels and how they are expected to threaten coastal populations worldwide. The study explains that as global temperatures rise, glaciers and polar ice caps are melting at an unprecedented rate, leading to higher sea levels that could submerge low-lying coastal areas. This is especially concerning for cities such as New York, Miami, Jakarta, and other coastal metropolises, where a significant portion of the population resides in areas just above sea level. The research further investigates the potential social and economic impacts on these regions, predicting displacement of millions of people, loss of infrastructure, and the onset of climate-induced migration.
    
    The study also covers the increasing frequency and intensity of extreme weather events. For example, it highlights how the Atlantic hurricane season has become longer and more destructive in recent years, with storms growing in size and intensity. Flooding, too, has become more common, with certain regions experiencing record-breaking rainfalls and rising river levels. Heatwaves are also more frequent, resulting in heat-related illnesses and a higher number of fatalities in vulnerable populations. The report draws connections between the increasing occurrence of these extreme events and the rise in greenhouse gas emissions, showing a direct link between human activities—such as fossil fuel consumption, deforestation, and industrial practices—and the intensification of these weather patterns.
    
    The research further discusses various climate models, both deterministic and probabilistic, which forecast different climate scenarios based on different levels of greenhouse gas emissions. These models attempt to predict the impact of various policy measures aimed at reducing emissions, including the global shift toward renewable energy sources and carbon capture technologies. The study underscores that without drastic reductions in carbon emissions, global temperatures could increase by as much as 4°C by the end of the century, leading to catastrophic changes in weather patterns and sea levels. However, it also presents scenarios where concerted global action could limit temperature increases to 1.5°C, in line with the Paris Agreement targets, thereby reducing the risks of some of the more extreme consequences.
    
    Your task is to extract all relevant information related to the correlation between greenhouse gas emissions and the rise in extreme weather events from the following study. Specifically, focus on:
    
    1.Key data points related to the rise in temperature and changes in regional weather patterns over the last 50 years.
    2.Statistical correlations provided in the study between greenhouse gas emissions and temperature fluctuations, including specific figures or graphs that show the direct relationship between these two variables.
    3.Information about specific regions that are projected to experience the most severe impacts due to climate change, and the related increase in frequency or intensity of extreme weather events such as hurricanes, floods, heatwaves, and droughts.
    4.Details on any natural disasters or extreme weather events mentioned in the report, including location, severity, and frequency, with relevant statistics or projections.
    5.The effects of rising sea levels and the expected consequences for coastal populations and cities, including data on expected sea level rise and projected impacts on infrastructure and population displacement.
    6.Information on the climate models used in the study, including the assumptions made, the predicted global temperature increases for various emission scenarios, and the potential social and economic impacts of these changes.
    7.Specific recommendations or proposed strategies for mitigating the effects of climate change, such as renewable energy adoption, emissions reduction targets, or investment in climate adaptation measures."
    """
    },

    {
        "tag":"Advanced Text Summarization","content":"""
    Text summarization is a critical task in natural language processing, as it helps in condensing large volumes of information into digestible and concise versions. Summarizing news articles, scientific papers, and books into shorter forms without losing key details is essential for time-strapped readers and researchers. In this exercise, you are asked to summarize an article discussing the global economic impact of artificial intelligence (AI) and automation on the labor market.
    
    The article highlights various factors, including the growing influence of AI on industries such as manufacturing, healthcare, finance, and education. It discusses the rapid advancements in automation technologies like robotics, machine learning algorithms, and natural language processing models, and how they are being implemented in different sectors to enhance productivity and efficiency. The article also addresses the potential job displacement caused by these technologies, especially for workers in roles that are highly repetitive and predictable, such as assembly line jobs, data entry tasks, and customer service.
    
    The article provides an in-depth analysis of how AI and automation are likely to reshape the future workforce. In particular, it explores the rise of new job categories that will emerge as a result of these technological advancements. For instance, the increasing demand for AI engineers, data scientists, machine learning specialists, and cybersecurity professionals is expected to create a wealth of new opportunities for skilled workers. However, the article also highlights the growing skills gap that may prevent many workers from transitioning to these new roles. It emphasizes the need for widespread retraining programs and educational reforms to equip the existing workforce with the skills needed to thrive in an AI-driven economy.
    
    Furthermore, the article discusses the potential societal implications of AI and automation, such as economic inequality, job polarization, and social unrest. It provides insights into the challenges that governments and organizations face in managing the widespread adoption of these technologies, while ensuring that the benefits of AI and automation are shared equitably across society. The article also examines potential policy interventions to address these challenges, such as universal basic income, taxation on automation, and the establishment of social safety nets for displaced workers.
    
    Another key aspect of the article is its focus on the ethical concerns surrounding the use of AI and automation. The article discusses the potential biases embedded in AI algorithms, the risks of surveillance, and the importance of ensuring transparency and accountability in AI systems. It also raises questions about the potential for AI to exacerbate existing inequalities, particularly in low-income and developing countries, where access to advanced technology may be limited. In addition, the article explores the implications of automation on workplace culture, including how human workers may need to adapt to collaborating with AI systems and automated machines in order to remain competitive in the job market.
    
    In your summary, provide a concise yet comprehensive overview of the article's key points. Focus on the economic impact of AI and automation, the potential consequences for the labor market, the rise of new job categories, and the ethical and societal concerns raised in the article. Avoid excessive detail, but ensure that the core themes and messages of the article are clearly conveyed.
        """
    },

    {
        "tag":"Advanced Information Extraction","content":"""
        Information extraction (IE) plays a crucial role in transforming unstructured text data into structured information that can be easily analyzed and utilized. In this task, you are required to extract specific information from a detailed scientific research paper on the effects of climate change on biodiversity in tropical rainforests.

    The paper provides a comprehensive study of how climate change has been impacting various species of flora and fauna in tropical rainforests, focusing on the Amazon, Congo, and Southeast Asian rainforests. The paper discusses the effects of rising global temperatures, changing precipitation patterns, and deforestation on the ecosystems and wildlife that inhabit these regions. It examines the role of these rainforests in regulating the global carbon cycle and their importance in mitigating the effects of climate change.
    
    The study emphasizes how increased temperatures and altered rainfall patterns have led to shifts in species' habitats, migration patterns, and reproductive cycles. Many species of plants and animals have been forced to adapt to these changes, while others have struggled to survive. For instance, certain species of amphibians and reptiles are particularly vulnerable to changes in temperature and humidity, leading to declines in their populations. Meanwhile, tropical trees have been affected by changes in precipitation, which impacts their growth rates and ability to absorb carbon dioxide.
    
    The paper also addresses the impact of deforestation, particularly in the Amazon rainforest, which has been rapidly shrinking due to agricultural expansion, logging, and infrastructure development. The loss of trees exacerbates the effects of climate change by reducing the rainforest's ability to sequester carbon and disrupts the habitats of countless species. In addition, the paper discusses the impact of human activities, such as mining and urbanization, which have led to habitat fragmentation and further stress on biodiversity.
    
    One of the key findings in the paper is that certain species are migrating toward higher altitudes or latitudes in response to changing environmental conditions. However, these species are often faced with barriers such as the lack of suitable habitats or the presence of competing species. The study notes that some species may become extinct if they cannot find new habitats, while others may form new ecological relationships as they encounter different species in the areas to which they migrate.
    
    The study also highlights the potential for ecosystem collapse if current trends in climate change and deforestation continue. It raises concerns about the long-term sustainability of tropical rainforests and the risks they pose to global biodiversity and climate regulation. The paper recommends urgent action to mitigate the effects of climate change and deforestation, such as implementing stricter environmental protection policies, reducing carbon emissions, and promoting sustainable land-use practices.
    
    Your task is to extract key information from this research paper, including:
    
    1.Specific impacts of climate change on species in the Amazon, Congo, and Southeast Asian rainforests.
    2.Details on the role of rainforests in the global carbon cycle and climate regulation.
    3.Information on how rising temperatures and changing precipitation patterns are affecting plant and animal species.
    4.Data on deforestation rates in the Amazon and its effects on biodiversity.
    5.Insights into species migration patterns, including those that are migrating to new regions due to climate change.
    6.Possible consequences of continued environmental degradation, such as species extinctions and ecosystem collapse.
    7.Policy recommendations for mitigating climate change effects and protecting biodiversity in tropical rainforests.
        """
        },

    {
        "tag":"Advanced Question Answering", "content":"""
        Question answering is a core task in natural language processing (NLP) that aims to provide concise and accurate answers to user queries based on large volumes of information. In this task, you are required to answer a complex question related to the field of renewable energy technologies and their role in combating climate change.

    The question is: 'What are the potential advantages and challenges of transitioning to renewable energy sources, such as wind, solar, and geothermal, as the primary means of meeting global energy demands?'
    
    The transition to renewable energy has been gaining momentum worldwide, as countries seek to reduce their reliance on fossil fuels and mitigate the impact of climate change. Renewable energy sources like solar, wind, and geothermal offer significant environmental benefits, including reducing greenhouse gas emissions, improving air quality, and decreasing dependence on nonrenewable energy sources.
    
    However, transitioning to renewable energy on a large scale presents several challenges that need to be addressed. One major challenge is the intermittent nature of renewable energy sources. Solar and wind energy, for example, depend on weather conditions and time of day, making it difficult to ensure a constant and reliable energy supply. This variability can be mitigated through energy storage technologies, such as batteries and pumped hydro storage, but these technologies are still developing and can be costly to deploy.
    
    Another challenge is the infrastructure required to support renewable energy generation. Large-scale deployment of solar panels, wind turbines, and geothermal plants requires significant investment in new infrastructure, including power grids, transmission lines, and energy storage facilities. This can be particularly challenging in regions with limited existing infrastructure or where land availability for renewable energy projects is restricted.
    
    The integration of renewable energy into the existing energy grid also requires careful planning to ensure that the grid remains stable and capable of handling fluctuating energy inputs. The challenge of balancing supply and demand in real-time, while maintaining grid reliability, requires advanced grid management systems and technologies like smart grids and demand response.
    
    In addition to these technical challenges, there are economic and political considerations that must be addressed. The transition to renewable energy requires significant financial investment, and the economic viability of renewable energy technologies varies depending on the region and the availability of natural resources. Governments must also implement supportive policies and incentives, such as subsidies and tax credits, to encourage the development of renewable energy projects and attract private investment.
    
    While renewable energy sources offer numerous environmental benefits, their widespread adoption also has social and economic implications. The transition to renewables will likely displace jobs in traditional fossil fuel industries, such as coal mining and oil drilling. However, the renewable energy sector is expected to create new job opportunities in areas such as solar panel manufacturing, wind turbine maintenance, and energy storage.
    
    Your task is to answer the question by addressing the following aspects:
    
    The environmental benefits of renewable energy, such as reducing greenhouse gas emissions and improving air quality.
    The challenges associated with the intermittent nature of renewable energy sources and potential solutions.
    The infrastructure and investment required for large-scale renewable energy deployment.
    The technological innovations needed to integrate renewable energy into the existing energy grid.
    The economic and political considerations of transitioning to renewable energy, including financial investment and government policies.
    The potential social and economic implications, including job displacement and the creation of new job opportunities in the renewable energy sector.
    """
    },

    {
        "tag":"Advanced Conversation","content":"""
        In this scenario, you are tasked with simulating an advanced conversation between a user and an AI assistant. The user is a university student studying environmental science, and they have a deep interest in understanding the ecological effects of climate change. The AI assistant must provide accurate, detailed, and well-reasoned responses to the user’s questions, and the assistant must be capable of explaining complex topics in an accessible manner, making sure to reference relevant research, studies, and data when applicable.

    The conversation will cover multiple topics related to climate change, including its causes, impacts on ecosystems and human health, adaptation strategies, and current global efforts to mitigate climate change. Below is a continuation of the conversation with the user’s questions and the AI assistant’s responses.
    
    User: "What are the primary human activities contributing to climate change, and how do they impact the atmosphere?"
    
    AI Assistant: "The primary human activities contributing to climate change are the burning of fossil fuels, deforestation, and agricultural practices. Fossil fuels—such as coal, oil, and natural gas—are burned for energy production and transportation, releasing large amounts of carbon dioxide (CO2) and methane (CH4) into the atmosphere. These gases are known as greenhouse gases because they trap heat within the Earth’s atmosphere, contributing to the greenhouse effect. As the concentration of these gases increases, global temperatures rise, leading to a variety of environmental and societal impacts.
    
    Deforestation is another major contributor to climate change. Trees absorb CO2 during photosynthesis, so when forests are cleared for agriculture or urbanization, this stored carbon is released into the atmosphere. Additionally, forest loss reduces the Earth’s ability to absorb future CO2 emissions, exacerbating the problem. Agricultural practices, particularly livestock farming, are also significant contributors to greenhouse gas emissions. Livestock such as cows and sheep produce methane as part of their digestive process, and the conversion of forests into agricultural land releases carbon stored in vegetation and soil."
    
    User: "What are some of the most noticeable effects of climate change on global ecosystems, and how are different ecosystems being affected?"
    
    AI Assistant: "The impacts of climate change on ecosystems are profound and widespread. Some of the most noticeable effects include:
    
    Rising Temperatures: Many ecosystems are experiencing shifts in temperature patterns, which affect species' behavior, reproduction, and survival. For example, coral reefs are highly sensitive to temperature changes, and even small increases in ocean temperatures can lead to coral bleaching, where the symbiotic algae that corals rely on are expelled, causing the coral to die. Similarly, warmer temperatures are altering migration patterns for species like birds, insects, and mammals, who rely on specific seasonal cues to move or reproduce.
    
    Changing Precipitation Patterns: Changes in rainfall are also affecting ecosystems. Some regions are experiencing more intense rainfall, leading to flooding and erosion, while others face prolonged droughts that reduce water availability for both wildlife and plants. These changes disrupt natural water cycles and can lead to the desertification of previously fertile areas, especially in regions like Sub-Saharan Africa.
    
    Sea Level Rise: Coastal ecosystems, including mangroves, estuaries, and salt marshes, are being threatened by rising sea levels. As sea levels rise, these ecosystems are submerged, which leads to the loss of habitat for countless species. In some areas, freshwater ecosystems are being contaminated with saltwater, making it difficult for freshwater species to survive.
    
    Loss of Biodiversity: Climate change is also driving species to extinction or forcing them to migrate to new areas. As temperatures rise, species are often forced to move toward cooler areas, either higher altitudes or higher latitudes. However, not all species can migrate fast enough, especially those that live in specific habitats like polar regions, where temperature changes are most drastic. The resulting loss of biodiversity undermines the stability of ecosystems and reduces their ability to provide essential services like pollination, water purification, and soil fertility.
    
    These effects highlight the interconnectedness of climate systems, ecosystems, and species survival, underscoring the urgency of addressing climate change."
    
    User: "What are the most promising solutions to mitigate climate change, and how can individuals contribute?"
    
    AI Assistant: "There are several promising solutions to mitigate climate change, ranging from policy changes to technological innovations, as well as individual actions. Here are some key strategies:
    
    Renewable Energy Transition: Transitioning from fossil fuels to renewable energy sources such as wind, solar, and hydroelectric power is one of the most critical steps in reducing carbon emissions. Renewable energy technologies are advancing rapidly, and their widespread adoption is essential for decarbonizing the global economy.
    
    Carbon Capture and Storage (CCS): CCS technologies capture CO2 emissions from power plants and industrial sources and store them underground. While still in the early stages, these technologies could play a significant role in reducing the amount of CO2 released into the atmosphere.
    
    Energy Efficiency: Improving energy efficiency in homes, buildings, and industries can reduce energy consumption and lower carbon emissions. This includes measures like using energy-efficient appliances, insulating buildings, and upgrading transportation systems to reduce fuel use.
    
    Reforestation and Afforestation: Planting trees and restoring degraded forests can help absorb carbon from the atmosphere. Forests act as carbon sinks, sequestering large amounts of CO2 over time. Large-scale reforestation initiatives are a key strategy for mitigating climate change.
    
    Sustainable Agriculture: Adopting more sustainable farming practices, such as regenerative agriculture, can reduce emissions from agriculture and enhance soil health. Techniques like no-till farming, crop rotation, and using fewer synthetic fertilizers can help sequester carbon and reduce emissions.
    
    As for individual actions, people can contribute by reducing their carbon footprint. Simple steps include using energy-efficient appliances, reducing car travel, adopting plant-based diets, and supporting policies that promote renewable energy and carbon reduction.
        """
    },

    {
        "tag":"Advanced Coding", "content":"""
        You are tasked with implementing a complex algorithm that performs real-time analysis of streaming data. The goal is to build a system capable of processing large amounts of data with minimal latency while maintaining high accuracy and robustness. In particular, your implementation should focus on creating an efficient solution that can detect patterns in real-time financial transactions, particularly detecting fraudulent activities.
    
    The system should handle a continuous stream of data from an API that provides transactional data, including information such as transaction ID, time, amount, location, and user account details. Your solution must have the capability to detect anomalies in real time and flag potential fraudulent activities. The system should be able to handle multiple transaction streams concurrently and execute the fraud detection analysis with high throughput.
    
    The transaction data might follow these general patterns:
    
    Transactions are associated with a user’s account and each transaction includes data such as user ID, transaction amount, time of the transaction, and the geographical location of the transaction.
    A user’s account might show multiple transactions within a short time span or across different locations.
    Fraudulent activities often manifest through rapid, repeated transactions or geographical inconsistencies, such as multiple transactions from different countries within a short time period.
    For the implementation:
    
    1.Data Stream Handling: You will need to establish a way to pull or receive data continuously from an API. You can simulate this by using a set of pre-recorded data that mimics the API’s transaction data. Design the system to handle incoming data in a way that doesn’t block the system while performing analysis. You should also implement a buffer or queue for handling the data stream.
    
    2.Fraud Detection Algorithm: Implement a machine learning model (such as decision trees, logistic regression, or an anomaly detection algorithm) to detect fraudulent transactions. You must also design and implement a rule-based system that uses heuristics such as the transaction frequency or location inconsistency to flag potential fraud. The model should be able to continually learn from new data and improve its prediction accuracy.
    
    3.Concurrency and Parallelism: Since financial data may come in at a high rate, you will need to use concurrency or parallelism to speed up the detection process. This might involve multi-threading or asynchronous processing in Python to handle multiple incoming transactions concurrently. Optimize your code to reduce delays between data receipt and fraud detection.
    
    4.Real-Time Alerts: If a fraudulent transaction is detected, the system should send an immediate notification or alert. The alerts should contain the relevant transaction details, such as the transaction ID, user ID, location, and the reason why the transaction was flagged. Alerts should be logged in a database for later review by security analysts.
    
    5.Performance and Scalability: The system should be able to scale, handling multiple transaction streams at once. Consider the efficiency of your solution—whether it can handle growing transaction volume, and whether it uses resources efficiently. You may need to benchmark and optimize your system to maintain low latency while processing a large number of transactions.
    
    6.The final deliverable should be a Python implementation using your choice of libraries for data handling, concurrency, and machine learning. The system must be capable of processing at least 1000 transactions per second without significant latency and flagging fraudulent activities in real time. Be sure to include comprehensive documentation of the system design, the fraud detection model, and how it processes transactions.
        """
    },

    {
        "tag" : "Advanced Reasoning", "content" : """
        Solve the following complex reasoning puzzles, and provide a detailed explanation of how you arrived at each conclusion. These problems require logical deduction and step-by-step analysis.
    
    Problem 1: In a room, there are three people: Alice, Bob, and Charlie. Each person has a unique role: one is a knight (always tells the truth), one is a liar (always lies), and one is a knave (alternates between truth and lies). Each of them makes one statement:   
    Alice: "I am the knight."
    Bob: "Charlie is the liar."
    Charlie: "Alice is the knight."
    Determine who is who and explain your reasoning. 
      
    Problem 2: A man has 100 gold coins. He needs to split them into 3 bags: one containing 40 coins, one containing 30 coins, and one containing 30 coins. He can only make two cuts. How can he do it?  
      
    Problem 3: You are in a room with a locked box that has two keys. One key will open the box, but the other key will trigger an alarm. You don’t know which key is which. You have two statements from two people:   
    Person A: "The key on the left will open the box."
    Person B: "Person A is lying."
    One person always tells the truth, and the other always lies. Which key opens the box?
    
    Solve each problem step-by-step and explain your reasoning in detail.
"""
    },

    {
      "tag":"Advanced Reasoning 2","content" : """
      Imagine you are tasked with designing an intelligent algorithm capable of solving complex, multi-step reasoning problems. The system must not only understand logical relationships between different elements but also apply various reasoning techniques to derive conclusions. In this scenario, you must develop an algorithm that can analyze a series of interconnected statements and make inferences based on logical deductions. The problem involves determining whether a series of hypotheses is consistent with a set of premises and whether conclusions can be derived based on those premises.

    The problem involves the following scenario: A company is planning a global expansion, and they need to decide which markets to enter based on various factors such as demand, competition, legal environment, and cost of entry. The task is to determine the most feasible market to enter based on the given data. However, the data provided has multiple inconsistencies and missing information, making the reasoning process more challenging.
    
    Scenario Overview: The company has identified four potential markets (Market A, Market B, Market C, and Market D) and has gathered data on several key factors. The company has to make a decision based on the following premises:
    
    Market A: This market has high demand but also high competition. The legal environment is moderately favorable, but the cost of entry is also high. The company has limited experience in this market.
    Market B: Market B has moderate demand and low competition. The legal environment is highly favorable, and the cost of entry is low. The company has some experience in this market.
    Market C: Market C has low demand but extremely low competition. The legal environment is very unfavorable, and the cost of entry is high. The company has no experience in this market.
    Market D: Market D has high demand and moderate competition. The legal environment is very favorable, and the cost of entry is moderate. The company has extensive experience in this market.
    Reasoning Task:
    
    Your task is to analyze the data and use logical reasoning to answer the following questions:
    
    Market Selection Criteria: Based on the given premises, which market should the company prioritize for expansion? Use logical deduction to determine which factors should carry the most weight (e.g., demand, competition, legal environment, cost of entry, or experience). Are there any trade-offs between these factors? If so, how can the company balance these conflicting factors to make the best decision?
    
    Inconsistencies and Missing Information: The provided data has several inconsistencies. For example, Market C has both low demand and an unfavorable legal environment, yet it still has a very low competition rate. Is this pattern logical? How can you resolve these inconsistencies using reasoning and assumptions? Could there be hidden opportunities or risks associated with Market C that are not immediately apparent from the data?
    
    Risk Assessment: Assess the risks associated with each market. For example, Market D has moderate competition and a favorable legal environment, but the company has extensive experience in this market. What are the potential risks associated with the company's experience in this market? Could the company's prior knowledge lead to complacency or overconfidence? How should these risks be factored into the decision-making process?
    
    Hypothetical Scenarios: Assume the company receives new data: Market B’s competition level increases, but demand also rises significantly. In addition, Market D’s legal environment becomes less favorable. How would these new developments affect your initial reasoning and the company’s decision? What new inferences can you draw based on these changes?
    
    Long-Term Strategy: The company is not only concerned with immediate profitability but also with long-term sustainability. Considering the potential for future growth, what factors should be prioritized in the company's expansion strategy? How would you apply reasoning techniques such as cost-benefit analysis and future forecasting to develop a long-term strategy?
    
    Global Expansion Factors: Consider the global implications of the company's decision. Beyond the market-specific factors, what global considerations should the company take into account, such as geopolitical risks, economic stability, and cultural factors? How might these global factors influence your reasoning and the decision-making process?
    
    Advanced Reasoning Approach:
    
    Deductive Reasoning: Deduce logical conclusions based on the premises. For example, if Market A has high competition but also high demand, how can you balance these two conflicting factors? Use deductive reasoning to form logical inferences.
    
    Inductive Reasoning: Generalize conclusions based on observed data. If Market D has high demand and moderate competition, but the cost of entry is moderate, can you predict that this market might be the best overall option?
    
    Hypothetical Reasoning: Consider how changes in one factor could alter the outcome. For example, what if the legal environment in Market B worsens? How would that change the reasoning process and the decision?
    
    Comparative Reasoning: Compare the different markets and the factors associated with them. Weigh the pros and cons of each option and make an informed decision. Use comparative reasoning to identify the most viable market for expansion.
    
    By utilizing a combination of these reasoning techniques, you can systematically analyze the data and make an informed decision regarding the best market for the company's global expansion."""
    },

    {"tag":"Lengthy and Complex Query","content" : """
    Imagine you are an interdisciplinary team of experts from the fields of Artificial Intelligence, Healthcare, Bioethics, and Regulatory Affairs, and your task is to conduct a detailed, multi-faceted analysis on the current and future impact of Artificial Intelligence (AI) on global healthcare systems, particularly in the context of patient care, medical research, public health policy, and the ethics surrounding AI technologies. Your analysis should address each of the following aspects in depth, with detailed explanations, historical context, potential future advancements, and real-world examples:

    1. Comprehensive Overview of AI in Healthcare:
    Define AI in the context of healthcare, explaining key technologies such as machine learning, deep learning, natural language processing (NLP), computer vision, and predictive analytics.
    Discuss the evolution of AI technologies in healthcare over the past two decades, providing specific examples of milestones and key developments that have shaped the current landscape.
    Compare and contrast AI-based solutions with traditional healthcare methods, highlighting the strengths and weaknesses of both approaches.
    2. AI-Driven Applications in Clinical and Public Health:
    Clinical Diagnostics: Provide an in-depth explanation of how AI technologies such as image recognition, diagnostic algorithms, and predictive models are being used in diagnosing diseases (e.g., cancer, heart disease, neurological disorders, etc.). Discuss the advantages and limitations, and reference specific AI-driven diagnostic tools used in hospitals and healthcare settings.
    Personalized Medicine: Explain how AI is enabling precision medicine, including its role in tailoring treatments to individual patients based on genetic information, lifestyle, and environmental factors. Discuss the potential and challenges of integrating AI into personalized treatment planning and the benefits for rare diseases.
    Drug Discovery & Development: Describe how AI and machine learning models are being used to accelerate the drug discovery process, highlighting the stages where AI provides substantial benefits (e.g., drug target identification, clinical trials, and FDA approval). Analyze the costs and ethical concerns associated with AI-driven pharmaceutical research.
    Public Health & Epidemiology: Examine the role of AI in epidemic prediction, vaccine development, and population health management, focusing on how AI models are helping predict the spread of diseases, manage health crises like pandemics (e.g., COVID-19), and optimize resource allocation in public health systems.
    3. Ethical Considerations in AI Healthcare Applications:
    Discuss the ethical implications of using AI in healthcare, focusing on issues such as data privacy, security, informed consent, and transparency in algorithms. How do these ethical considerations differ when dealing with sensitive health data, such as genomic or mental health information?
    Bias in AI Models: Analyze the dangers of bias in AI healthcare models, particularly in relation to underserved populations, racial minorities, and gender disparities. How do AI biases potentially exacerbate healthcare inequalities? What are some methods to mitigate bias in AI algorithms and ensure equitable access to healthcare?
    Accountability and Responsibility: Discuss who is responsible when AI systems make erroneous healthcare decisions—healthcare providers, AI developers, or regulatory bodies? Provide examples of real-world situations where AI systems have made significant mistakes in healthcare and what the legal and ethical consequences were.
    4. Regulation, Legal, and Policy Frameworks for AI in Healthcare:
    Discuss the regulatory landscape surrounding AI technologies in healthcare, including the role of national and international regulatory bodies like the FDA (U.S. Food and Drug Administration), EMA (European Medicines Agency), and WHO (World Health Organization). Explain the differences between the regulations for AI in medical devices, clinical decision support systems, and digital therapeutics.
    Analyze the challenges of regulating AI in healthcare, especially with rapidly advancing technologies and AI systems that are constantly learning and evolving. What legislative frameworks and regulatory models are being proposed or adopted around the world to deal with AI in healthcare?
    Explain the concept of AI explainability and transparency in healthcare, and discuss why it is crucial to develop AI systems that both clinicians and patients can understand and trust.
    5. Future Trends and Breakthroughs in AI and Healthcare:
    Quantum Computing and AI: Speculate on how quantum computing could enhance AI models in healthcare, especially in areas requiring massive data processing like genomics, molecular modeling, and multi-modal diagnostics.
    AI and Robotics in Surgery: Explore how AI-powered robotics is changing the landscape of surgery, focusing on key innovations like robotic-assisted surgery, minimally invasive procedures, and autonomous surgical robots. What are the benefits, risks, and regulatory challenges of using autonomous robotic systems in healthcare?
    AI and Neurotechnology: Discuss the future potential of neurotechnology and AI in fields such as brain-computer interfaces, mental health diagnostics, and neurological disorder treatment. Include speculative applications in treating conditions like Alzheimer's, Parkinson's, and depression.
    AI-Driven Personalized Health Monitoring: Analyze how wearable devices, smart implants, and other AI-powered health monitoring systems are revolutionizing chronic disease management, elderly care, and preventative healthcare. Discuss potential challenges in data privacy, integration with existing healthcare infrastructure, and patient acceptance.
    6. Economic and Societal Impact of AI in Healthcare:
    Discuss the economic implications of integrating AI into healthcare systems globally. How does AI influence healthcare costs, efficiency, and resource allocation? Consider both the positive impacts (e.g., cost savings, improved care) and negative aspects (e.g., displacement of healthcare jobs, access disparities).
    Examine the impact on healthcare workers: Will AI lead to job displacement for healthcare professionals, or will it augment their abilities to provide better care? How can healthcare professionals be trained to work alongside AI tools effectively? What new roles may emerge in the AI-powered healthcare ecosystem?
    Analyze the social implications of AI in healthcare, focusing on issues of accessibility (to cutting-edge treatments, diagnostic tools), trust, and health literacy among patients. How can AI be used to improve healthcare access for rural, marginalized, or low-income populations?
    7. Challenges and Barriers to Widespread AI Adoption in Healthcare:
    Examine the technical barriers to widespread AI adoption, such as data interoperability, the availability of high-quality healthcare data, and the integration of AI models into legacy healthcare infrastructure.
    Trust and Public Perception: Analyze the public’s perception of AI in healthcare. How can health systems build public trust in AI technologies? Consider aspects such as transparency, explainability, and the involvement of healthcare professionals in the decision-making process.
    Discuss the economic and policy barriers, including the high costs of AI development, regulatory hurdles, and the resistance from healthcare providers to adopt new technologies. What initiatives are needed to overcome these barriers?
    8. Global Perspective:
    Discuss how AI in healthcare is being adopted in different parts of the world, such as North America, Europe, Asia, and Africa. How do different regions face unique challenges and opportunities regarding AI healthcare implementation?
    Compare AI adoption rates between developed and developing countries. What role does global health inequality play in AI accessibility?
    Conclusion: "Summarize your analysis and provide an outlook on the most promising applications of AI in healthcare over the next 5, 10, and 20 years. What steps should be taken today to ensure that AI can be safely and ethically integrated into healthcare systems worldwide?
    """
     }
]
