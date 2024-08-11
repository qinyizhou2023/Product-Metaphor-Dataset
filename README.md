# ProductMetaphor Dataset

## Overview

We introduce a dataset of extended metaphors for product design.

* The labels for metaphors were collected from websites and papers about metaphorical product design, considering: 1) TARGET-SOURCE pairs, 2) mapping strategies, and 3) meaning. 
* We conducted a comprehensive evaluation of state-of-the-art zero-shot GPT-4 models on metaphor understanding tasks based on 80 classical metaphorical product design images.
* The result shows that...

### [product_metaphor_list](product_metaphor_list.csv)
 150 product metaphors that consist of XXX:
* image_path: the product's image
* name: the products' name
* target: the target product
* source: the source product
* way of connection: The connection between the source with the target, including:
![img_1.png](img_1.png)
* connection: A scentence conveying the connection between the target and source
* way of mapping: the mapping attribute ( choose from: form, function, interaction)
* detail mapping: other properties that help to forster the metaphor expression
  ![img_2.png](img_2.png)

### GPT_result


### Expert_rate
 
* Fluency: The metaphor is fluent, grammatical, and easy to understand.
* Scientific Precision: The reasons for the metaphor explain the scientific concepts precisely.
* Relatedness: The reasons for the metaphor closely connect the scientific concepts and metaphorical concepts.
* Validity: The reasons for the metaphor are valid overall. They perform a role as a scientific metaphor explaining the scientific concept in a more understandable and relatable way.
* Willingness to adopt: I'm willing to use this metaphor for my writing. 
* Inspirational effect: The metaphor example will inspire me to create metaphors.



## Files

* rating_vehicle.csv: professional writers' ratings on vehicles of metaphors
* rating_mapping.csv: professional writers' ratings on mappings of metaphors
* concepts_per_domain.csv: mapping between the scientific domains and scientific concepts

## Licensing

Labels are licensed under Creative Commons Attribution 4.0 License

## Contact

This section will be added after the blind review process.

## Citations

```
Jeongyeon Kim, Sangho Suh, Lydia Chilton, and Haijun Xia. "Metaphorian: Leveraging Large Language Models to Support Extended Metaphor Creation for Science Writing." In Designing Interactive Systems Conference, pp. 41-57. 2023.
```

```
@inproceedings{kim2023metaphorian,
  title={Metaphorian: Leveraging Large Language Models to Support Extended Metaphor Creation for Science Writing},
  author={Kim, Jeongyeon and Suh, Sangho and Chilton, Lydia and Xia, Haijun},
  booktitle={Designing Interactive Systems Conference},
  pages={41--57},
  year={2023}
}
```
