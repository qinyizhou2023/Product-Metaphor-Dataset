# ProductMetaphor Dataset

## Overview
To gain a deeper understanding of the design patterns and methods employed in each phase of metaphorical design, particularly how designers identify sources and develop mapping strategies, we conducted an extensive analysis of metaphorical product design cases. Our dataset comprises 150 examples of metaphorical product designs collected from the official websites of prominent design companies like Alessi and Nendo, as well as from design competitions and platforms such as Red Dot Design and Pinterest. The focus is on home accessories that exemplify the use of product metaphors.

This dataset introduces a collection of extended metaphors in product design:

- **Data Collection:** Metaphor examples were gathered from websites and academic papers focused on metaphorical product design.
- **Product Categories:** The products fall under the criteria of being small in size, simple in function, widely available, and possessing significant design potential. All products analyzed belong to the 164 categories listed in Amazon's household section. For each product, we collected the official product description from the original websites.
- **Annotation:** Two professional product designers annotated the ways of connection and mapping methods.
- **Descriptions:** The connection and mapping descriptions are based on the official product introductions available on their respective websites.

[//]: # (- **Evaluation:** We conducted a comprehensive evaluation of state-of-the-art zero-shot GPT-4 models on metaphor understanding tasks using 150 classical metaphorical product design images, with the results showing that...)

### [product_metaphor_list](product_metaphor_list_3level.csv)
The dataset contains 150 product metaphors with the following attributes:

[//]: # (- **image_path:** Path to the product's image.)
- **name:** The product's name.
- **target:** The target.
- **source:** The source.
- **way_of_connection:** The type of connection between the source and the target, categorized into categorized into (refer to)[^1]::
  1. **Visceral:** Based on similarity in shape, color, or structure, evoking an immediate emotional response from users.
     - **Connection Format:** 
       - "B visually resembles A, evoking [specific emotion or feeling] in [A's target users]."
       - "B is as [adjective] as A."
  2. **Behavioral:** Based on similarities in interaction, function, and behavior, enhancing the target's usability or utility.
     - **Connection Format:** 
       - "Both B and A + verb. + adv. / in a similar manner."
       - "[B + verb] like [A + verb]."
       - "Both B and A allow for [specific interaction] similarly."
       - "[Interacting with B] behaves like [interacting with A]."
  3. **Reflective:** The inclusion of the source influences the product's usage context and conveys a new meaning for using it.
     - **Connection Format:** 
       - "B is inspired by [legend/story]."
       - "Both B and A symbolize/associate with [specific cultural meaning]."
       - "B creates an [adjective] experience in [specific using environment]."
       - "B symbolizes/promotes [concept/thoughts] for A/as using A."
       - "B transforms [A's usage experience] into a [new experience]."
- **Connection:** A sentence describing the connection between the target and the source, following the format above.
- **way_of_mapping:** The mapping attributes, chosen from Vision, Usage, Touch, Sound, Smell, and Taste.
- **mapping_strategy:** A sentence describing the mapping strategy between the target and the source, following these formats:
  1. **Vision:** "A's [property] looks like B's [property]."
  2. **Usage:** "A's [property] is used like B's [property]."
  3. **Touch:** "A's [property] feels like B's [property]."
  4. **Sound:** "A's [property] sounds like B's [property]."
  5. **Smell:** "A's [property] smells like B's [property]."
  6. **Taste:** "A's [property] tastes like B's [property]."
- **detail_mapping:** Additional properties that enhance metaphor expression, chosen from: Color, Style, Size, Structure, Graphics, Light and Shadow, Function, Interaction/Movement, Texture, Material, Temperature, Sound, Taste, Smell.

![img_3.png](img_3.png)

[^1]: Don Norman. 2007. Emotional design: Why we love (or hate) everyday things. Basic Books.




## Citations

```
Qinyi Zhou, Jie Deng, Yu Liu, Yun Wang, Yan Xia, Yang Ou, Zhicong Lu, Sai Ma, Scarlett Li, and Yingqing Xu. 2025. ProductMeta: An Interactive System for Metaphorical Product Design Ideation with Multimodal Large Language Models. In Proceedings of the 2025 CHI Conference on Human Factors in Computing Systems (CHI '25). Association for Computing Machinery, New York, NY, USA, Article 428, 1–24. https://doi.org/10.1145/3706598.3713935```

```
@inproceedings{10.1145/3706598.3713935,
author = {Zhou, Qinyi and Deng, Jie and Liu, Yu and Wang, Yun and Xia, Yan and Ou, Yang and Lu, Zhicong and Ma, Sai and Li, Scarlett and Xu, Yingqing},
title = {ProductMeta: An Interactive System for Metaphorical Product Design Ideation with Multimodal Large Language Models},
year = {2025},
isbn = {9798400713941},
publisher = {Association for Computing Machinery},
address = {New York, NY, USA},
url = {https://doi.org/10.1145/3706598.3713935},
doi = {10.1145/3706598.3713935},
abstract = {Product metaphors, which involve creating products that convey meaning through metaphorical associations, are a powerful tool in product design. However, according to our formative study, novice designers often struggle to establish coherent links between target and source, to manage the complexity of diverse mapping possibilities, and to balance product usability with metaphorical expression. To address these challenges, we introduce ProductMeta, a creativity support tool designed to support novice designers in exploring and developing metaphorical product designs. ProductMeta incorporates domain knowledge and decomposes the design process into iterative modules and framework-based interfaces, fostering both divergent and convergent thinking. Through user studies, we demonstrate that ProductMeta enables novice designers to generate diverse and contextually relevant design ideas by facilitating structured exploration. We conclude with design implications for human-AI co-creation.},
booktitle = {Proceedings of the 2025 CHI Conference on Human Factors in Computing Systems},
articleno = {428},
numpages = {24},
keywords = {Creativity support tool, Product Design Ideation, Metaphor Design, Machine Learning},
location = {
},
series = {CHI '25}
}
```

