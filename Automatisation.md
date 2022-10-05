# automation

## problem

A photographer is in constant need to stay in touch with latest technological advancements. There's the constant evaluation of the added value a professional photographer has against people using their own camera or even smartphone.

If we can cut down on tasks which are not of added value, a photographer is able to maintain a healty value-cost balance towards clients. Therefore in the first part of the PWO we investigate how AI will transform the workflow and workload of a photographer, in the specific tasks which can be automated.

### context
A photographer has a workflow in the software (s)he knows. Two popular programs are photoshop & lightroom. For both programs a possible workflow is depicted, a reader can image that a photo is moving from step to step to be adapted by the photographer.
We'll implement for each of there steps an AI/ML model to be able to process the pictures in batch and without lots of manual intervention needed. These models do operate separately from the software packets. The software packets are merely shown as an indication of a possible workflow and thus what a photographer would expect to be able to do with images.

## implementation & consequences

the implementation is heavy on the tech side: we make use of google colab for remote processing power and nextcloud as a server solution for data storage. We implement open source machine learning algorithms, thus the only UI we have right now are some parameters tweakable in the different google colabs.
This tech heavy side is chosen as we want to know and show what's going on under the hood of a machine learning based solution. 
It is to be expected that the big software packets start to implement a lot of these tools rather quick, as the research community is taking big steps in these directions and tools for some of these problems are popping up at frequent pace.

## workflows


### lightroom

![lookbook](./images/Timeline_LB_Retouching_Lightroom.png)
### photoshop flow
![lookbook](./images/Timeline_LB_Retouching_Photoshop.png)

### photoshop flow with the chosen machine learning models
![flow](./images/Timeline_LookBook_Flow.png)

## Research questions

1. How can we integrate open-source machine learning models within the current workflow of photographers, and put these models to work to free lens-based creatives of repetitive and labour-intensive tasks?
2. To what extent does the workfield think or hope that AI/ML would change their future craft?
3. Can AI be of value as a creative stimuli in the creation of a lookbook?

## comparison with SOTA

|metric|our solution|lightroom|photoshop|luminar|capture one|
|---|---|---|---|---|---|
|batchmode| auto | 1/2 auto* | 1/2 auto* | 1/2 auto* | 1/2 auto* |
|sensor dust| auto | 1/2 auto* | manual | auto | 1/2 auto* |
|image cleanup|manual| manual | manual | manual | manual |
|background removal| auto | 1/2 auto | 1/2 auto | 1/2 auto | - |
|background replacement| auto | manual | manual | manual | - |
|clothes recoloring |-| x | x | x | - |
|skin correction| auto | manual | 1/2 auto | auto | manual |
|color correction: dodge & burn|-| manual | manual | manual | manual |
|color corrections: levels,contrast & curves | auto | 1/2 auto* | 1/2 auto* | 1/2 auto* | 1/2 auto* |
|color grading| auto | 1/2 auto* | 1/2 auto* | 1/2 auto* | 1/2 auto* |
|image upscaling| semi auto | x | x | x | x |
|noise| semi auto | manual | manual | manual | manual |

 (* preset)



## Metrics

in order to evaluate the results of an image, we want some metrics to evaluate. Not every result or image is useful or wanted for all targets.

| target     | resolution px | other metrics (e.g. | DPI |  
| ---------- | ------------- | ------------------- | --- |
| smartphone | ≥ 750x1334    |                     | 326 |
| smartphone | ≤ 1440x3120   |                     | 564 |
| laptop     | ≥ 1080x1920   |                     | 72  |
| laptop     | ≤ 3000x2000   |                     | 72  |
| lookbook 1 | 816x1056      | 215.9x279.4 mm (A4) | 96  |
| lookbook 2 | 528x816       | 139.7x215.9 mm (A5) | 96  |
| lookbook 1 | 2550x3300     | 215.9x279.4 mm (A4) | 300 |
| lookbook 2 | 1650x2550     | 139.7x215.9 mm (A5) | 300 |
| IG-post SQ | 1080x1080     |                     | 72  |
| IG-post H  | 1200x608      |                     | 72  |
| IG-post V  | 1080x1350     |                     | 72  |
| IG-story   | 1080x1920     |                     | 72  |
