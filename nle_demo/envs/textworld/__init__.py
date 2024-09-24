from nle_demo.envs.textworld.textworld_factory import TextWorldFactory

TEXTWORLD_FACTORY = None


def global_textworld_context(cfg) -> TextWorldFactory:
    global TEXTWORLD_FACTORY
    if TEXTWORLD_FACTORY is None:
        TEXTWORLD_FACTORY = TextWorldFactory(
            objective=cfg.objective,
            description=cfg.description,
            score=cfg.score,
            max_score=cfg.max_score,
            won=cfg.won,
            max_episode_steps=cfg.max_episode_steps,
            textworld_games_path=cfg.textworld_games_path,
        )
    return TEXTWORLD_FACTORY
