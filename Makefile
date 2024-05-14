all: images/heat_diffusion.gif

images/heat_diffusion.gif: heat_diffusion.mp4
	ffmpeg -y -i heat_diffusion.mp4 -vf "fps=10,scale=320:-1:flags=lanczos" -loop 0 images/heat_diffusion.gif

.PHONY: heat_diffusion.mp4
heat_diffusion.mp4:
	python3 simulate.py heat_diffusion
