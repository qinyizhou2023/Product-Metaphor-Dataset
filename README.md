# ProductMetaphor Dataset

## Overview
To gain a deeper understanding of the design patterns and methods employed in each phase of metaphorical design, particularly how designers identify sources and develop mapping strategies, we conducted an extensive analysis of metaphorical product design cases. Our dataset comprises 150 examples of metaphorical product designs collected from the official websites of prominent design companies like Alessi and Nendo, as well as from design competitions and platforms such as Red Dot Design and Pinterest. The focus is on home accessories that exemplify the use of product metaphors.

This dataset introduces a collection of extended metaphors in product design:

- **Data Collection:** Metaphor labels were gathered from websites and academic papers focused on metaphorical product design, with primary sources including product design studios and Pinterest.
- **Product Categories:** The products fall under the criteria of being small in size, simple in function, widely available, and possessing significant design potential. All products analyzed belong to the 164 categories listed in Amazon's household section. For each product, we collected (1) a design image, with multiple images included when necessary to convey behavioral-level connections, and (2) the official product description from original websites.
- **Annotation:** Two professional product designers annotated the ways of connection and mapping methods.
- **Descriptions:** The connection and mapping descriptions are based on the official product introductions available on their respective websites.
- **Evaluation:** We conducted a comprehensive evaluation of state-of-the-art zero-shot GPT-4 models on metaphor understanding tasks using 150 classical metaphorical product design images, with the results showing that...

### [product_metaphor_list](product_metaphor_list_3level.csv)
The dataset contains 150 product metaphors with the following attributes:
- **image_path:** Path to the product's image.
- **name:** The product's name.
- **target:** The target product.
- **source:** The source product.
- **way_of_connection:** The type of connection between the source and the target, categorized into (A=Target; B=Source):
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

### GPT_result




## Files


## Licensing



## Contact

This section will be added after the blind review process.

## Citations

