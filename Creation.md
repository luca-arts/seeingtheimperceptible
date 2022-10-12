# Creation

## Limitations

### images with faces
A lot of online models do limit the end-user in what types of photo to use and to generate. Typically for generation they refuse NSFW images, biasing images (Hitler etc) .
For starting point, images with faces are not allowed (among others to try to evade deepfakes, fake news etc). Now for a photographer this is often requested. We'll take a look in how to approach this limitation. #todo




## Use AI with a unique photographers style
challenge: create/alter 10 photos with differing topics, make sure they have a recognisable style.

1. transfer learning with existing dataset of photographer?
2. choose the right words fitting to your style
	1. get to know your style ==> if you're not aware of your style yet or want to expand knowledge
		1. keywords? https://github.com/KBNLresearch/keyword-generator
		2. img to prompt?
3. Start with base images depicting your style
	1. e.g. placement of lights
4. style transfer (lesser option? as this is more an afterthought)
5. ?


## Pose generation
Challenge: generate 5 different poses based on 1 or more images (of same photoshoot)

1. Dall-E 2 or stable diffusion
2. openpose
3. ...