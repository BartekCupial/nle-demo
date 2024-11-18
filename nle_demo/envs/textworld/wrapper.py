import textwrap
from typing import Any, Tuple

import gym
import numpy as np
from PIL import Image, ImageDraw, ImageFont


class TextWorldWrapper(gym.Wrapper):
    def __init__(self, env: gym.Env):
        super().__init__(env)
        # dummy spaces
        self.observation_space = gym.spaces.Discrete(1)
        self.action_space = gym.spaces.Discrete(1)
        self.current_seed = None

    @property
    def unwrapped(self):
        return self

    def get_seeds(self):
        return self.current_seed

    def seed(self, seed):
        self.current_seed = seed
        return super().seed(seed=seed)

    def reset(self, **kwargs) -> Any | tuple[Any, dict]:
        obs, infos = super().reset(**kwargs)
        self.obs_history = [obs]
        return obs

    def step(self, action: Any) -> Tuple[Any, float, bool, dict]:
        obs, reward, done, info = super().step(action)
        self.obs_history.append(obs)
        return obs, reward, done, info

    def render_image(self):
        return np.asanyarray(render_textworld_to_image("\n".join(self.obs_history)))


def render_textworld_to_image(
    text, width=800, height=600, font_size=12, bg_color=(0, 0, 0), text_color=(255, 255, 255)
):
    # Create new image with background
    image = Image.new("RGB", (width, height), bg_color)
    draw = ImageDraw.Draw(image)

    # Load a monospace font (you'll need to specify a valid font path)
    try:
        font = ImageFont.truetype("DejaVuSansMono.ttf", font_size)
    except:
        # Fallback to default font
        font = ImageFont.load_default()

    # Calculate how many characters can fit per line
    char_width = font.getlength("m")  # Use 'm' as reference
    chars_per_line = int(width / char_width)

    # Split text into lines
    lines = text.split("\n")
    wrapped_lines = []
    for line in lines:
        # Wrap each line to fit width
        wrapped = textwrap.fill(line, width=chars_per_line)
        wrapped_lines.extend(wrapped.split("\n"))

    # Calculate line height
    line_height = font_size + 4

    # Calculate how many lines can fit
    max_lines = height // line_height

    # Keep only the lines that will fit (from the end)
    if len(wrapped_lines) > max_lines:
        wrapped_lines = wrapped_lines[-max_lines:]

    # Draw text
    y = 10
    for line in wrapped_lines:
        draw.text((10, y), line, font=font, fill=text_color)
        y += line_height

    return image
