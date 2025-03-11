class Package:
    """
    Class that represents a package with dimensions in centimeters and mass in kilograms.
    """
    def __init__(self, width_cm: float, height_cm: float, length_cm: float, mass_kg: float):
        """
        Initializes a new package.

        Args:
            width_cm (float): Width of the package in centimeters
            height_cm (float): Height of the package in centimeters
            length_cm (float): Length of the package in centimeters
            mass_kg (float): Mass of the package in kilograms
        """
        self.width_cm = width_cm
        self.height_cm = height_cm
        self.length_cm = length_cm
        self.mass_kg = mass_kg

        # EDGE CASES
        if self.width_cm < 0 or self.height_cm < 0 or self.length_cm < 0 or self.mass_kg < 0:
            raise ValueError("Dimensions and mass cannot be negative")

    @property
    def volume_cm3(self) -> float:
        """
        Calculates the volume of the package in cubic centimeters.
        """
        return self.width_cm * self.height_cm * self.length_cm

    def is_bulky(self) -> bool:
        """
        Determines if the package is bulky.
        A package is bulky if:
        - Its volume is >= 1,000,000 cm³, or
        - Any of its dimensions is >= 150 cm
        """
        return (self.volume_cm3 >= 1_000_000 or
                self.width_cm >= 150 or
                self.height_cm >= 150 or
                self.length_cm >= 150)

    def is_heavy(self) -> bool:
        """
        Determines if the package is heavy.
        A package is heavy if its mass is >= 20 kg
        """
        return self.mass_kg >= 20

    def sort(self) -> str:
        """
        Determines the stack where the package should go.
        Returns:
            str: 'STANDARD', 'SPECIAL' or 'REJECTED' based on package characteristics
        """
        if self.is_bulky() and self.is_heavy():
            return "REJECTED"

        if self.is_bulky() or self.is_heavy():
            return "SPECIAL"

        return "STANDARD"
