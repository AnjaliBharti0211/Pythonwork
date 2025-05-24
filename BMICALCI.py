# BMI Calculator - Beginner Project
# Created by Anjali ✨

import os
import time

try:
    from colorama import Fore, Style, init
    init(autoreset=True)
except ImportError:
    Fore = Style = lambda x: ""

def print_slow(text, delay=0.02):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

os.system('cls' if os.name == 'nt' else 'clear')

print(Fore.CYAN + Style.BRIGHT + "\n💪 Welcome to the BMI Calculator 🧠\n")

try:
    weight = float(input("🔢 Enter your weight in kilograms (kg): "))
    height = float(input("📏 Enter your height in centimeters (cm): "))
except ValueError:
    print(Fore.RED + "❌ Invalid input. Please enter numeric values.")
    exit()
bmi = round(weight / (height * height) * 10000, 2)
print(f"\n🧾 Your Body Mass Index (BMI) is: {Fore.YELLOW}{bmi}{Style.RESET_ALL}")
print(Fore.MAGENTA + "\n📋 Health Category:")

if bmi < 18.5:
    print(Fore.BLUE + "🔹 Underweight")
    print("💬 Tip: Kuch khaya piya karo 🥺")
elif 18.5 <= bmi <= 24.5:
    print(Fore.GREEN + "✅ Normal")
    print("💬 Tip: Great going! Avoid junk food 🍎")
elif 24.5 < bmi <= 29.5:
    print(Fore.YELLOW + "⚠️ Overweight")
    print("💬 Tip: Focus on a healthier diet and light exercise 🧘‍♀️")
elif 29.5 < bmi <= 34.5:
    print(Fore.RED + "🔴 Obesity Class 1")
    print("💬 Tip: Time to make health a priority 💪")
elif 34.5 < bmi <= 39.5:
    print(Fore.RED + "🔴 Obesity Class 2")
    print("💬 Tip: Strongly consider consulting a healthcare provider 🩺")
else:
    print(Fore.RED + "🔴 Obesity Class 3")
    print("💬 Tip: Please seek medical advice ASAP 🙏")

print(Fore.CYAN + "\n✨ Thank you for using the BMI Calculator! Stay healthy, stay happy! 🌟")         
