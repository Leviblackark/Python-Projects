import random


class Shape:
    def __init__(self, blob, space_between):

        self.colour = ["#8B4513", "#FF8C00", "#DDA0DD", "#9370DB", "#8FBC8F", "#4682B4",
                       "#FFEBCD", "#8B008B", "#FF4500", "#8B0000", "#20B2AA", "#FFD700",
                       "#90EE90"]
        self.dark_moody_colors = [
            # Deep Reds
            "#8B0000",  # Dark Red
            "#6B0F1A",  # Oxblood
            "#400D12",  # Dark Burgundy

            # Rich Purples
            "#4B0082",  # Indigo
            "#5D3A72",  # Deep Violet
            "#301934",  # Dark Mulberry

            # Shadowy Blues
            "#2C3E50",  # Midnight Blue
            "#1B263B",  # Prussian Blue
            "#0D1A26",  # Eclipse

            # Forest Greens
            "#013220",  # Deep Forest Green
            "#223A31",  # Moss Green
            "#1C3A3E",  # Teal Green

            # Earthy Browns
            "#3E2723",  # Dark Wood Brown
            "#5D4037",  # Walnut
            "#2B1B1B",  # Charred Brown

            # Stormy Greys
            "#4E4E50",  # Ash Grey
            "#232931",  # Charcoal Grey
            "#1C1C1E",  # Obsidian

            # Muted Golds
            "#8A795D",  # Antique Gold
            "#716040",  # Brass
            "#4A3C24",  # Burnished Bronze

            # Blackened Shades
            "#101820",  # Rich Black
            "#0F0F0F",  # Jet Black
            "#191919",  # Pitch Black

            # Dusky Pinks
            "#5A3E4F",  # Dusky Rose
            "#7D5360",  # Muted Mauve
            "#402639",  # Dark Plum

            # Other Shadows
            "#353535",  # Graphite
            "#252627",  # Onyx
            "#202124"  # Carbon
        ]

        self.blob = blob
        self.space_between = space_between

    def maker(self):
        """Progressively create shapes with the sides from 3 to 10"""

        for sides in range(3, 11):
            self.blob.color(random.choice(self.dark_moody_colors))
            angle = 360 / sides
            self.blob.pensize(2)

            # Within each number create shape before moving to the next stage
            for _ in range(sides):
                self.blob.speed("fastest")
                self.blob.forward(self.space_between)
                self.blob.right(angle)
                # self.blob.circle(5)

    def walker(self):
        """line that changes direction"""

        directions = [0, 90, 180, 270]

        self.blob.pensize(4)
        self.blob.speed("fastest")

        for _ in range(60):
            self.blob.pencolor(random.choice(self.dark_moody_colors))
            self.blob.forward(30)
            self.blob.setheading(random.choice(directions))

    def nested_shapes(self):
        """Shape gets bigger each time it goes round"""
        for _ in range(3, 8):  # Layers of shapes
            angle = 360 / _
            for _ in range(_):
                self.blob.forward(self.space_between)
                self.blob.right(angle)
                self.blob.shape("turtle")
                self.blob.stamp()
            self.space_between += 10  # Increment space for the next shape

    def firework(self):
        for _ in range(36):
            """Disc of lines in a circle shape"""
            self.blob.color(random.choice(self.dark_moody_colors))
            self.blob.forward(100)
            self.blob.backward(100)
            self.blob.right(10)
            self.blob.shape("turtle")
            self.blob.stamp()
