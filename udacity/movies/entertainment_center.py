# -*- coding: utf-8 -*-
import media
import fresh_tomatoes

toy_story = media.Movie(
    "Toy Story",
    "In a world where toys are living things who pretend to be lifeless" +
    "when humans are present, a group of toys, owned by six-year-old Andy " +
    "Davis, are caught off-guard when Andy's birthday party is moved up a " +
    "week, as Andy, his single mother and infant sister Molly are preparing " +
    "to move the following week.",
    "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
    "https://www.youtube.com/watch?v=KYz2wyBy3kc")

# print toy_story.storyline

avatar = media.Movie(
    "Avatar",
    "By 2154, humans have depleted Earth's natural resources, leading to a " +
    "severe energy crisis. The Resources Development Administration " +
    "(RDA for short) mines for a valuable mineral – unobtanium – on " +
    "Pandora, a densely forested habitable moon orbiting the gas giant " +
    "Polyphemus in the Alpha Centauri star system.[10] Pandora, whose " +
    "atmosphere is poisonous to humans, is inhabited by the Na'vi, 10-foot " +
    "tall (3.0 m), blue-skinned, sapient humanoids[33] who live in harmony " +
    "with nature and worship a mother goddess called Eywa",
    "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
    "https://www.youtube.com/watch?v=5PSNL1qE6VY")

# print avatar.storyline
# avatar.show_trailer()
movies = [toy_story, avatar]
fresh_tomatoes.open_movies_page(movies)
# print media.Movie.__doc__
