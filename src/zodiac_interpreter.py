from textx import metamodel_from_file
import datetime
import pytz
from src.zodiac_grammar import zodiac_metamodel


class ZodiacInterpreter:
    def __init__(self):
        self.variables = {}
        self.functions = {}
        self.return_value = None
        self.zodiac_data = {
            "Aries": {
                "date_range": "March 21 - April 19",
                "element": "Fire",
                "ruling_planet": "Mars",
                "traits": ["Bold", "Competitive", "Passionate", "Independent", "Impulsive"],
                "strengths": ["Leadership", "Courage", "Enthusiasm", "Determination"],
                "weaknesses": ["Impatience", "Moodiness", "Short temper", "Impulsivity"],
                "compatibility": ["Leo", "Sagittarius", "Gemini"],
                "male": "The Aries man is energetic and action-oriented. He's a natural leader with a competitive spirit.",
                "female": "The Aries woman is fiercely independent and passionate. She's ambitious and not afraid to take charge."
            },
            "Taurus": {
                "date_range": "April 20 - May 20",
                "element": "Earth",
                "ruling_planet": "Venus",
                "traits": ["Patient", "Reliable", "Devoted", "Practical", "Stubborn"],
                "strengths": ["Dependability", "Persistence", "Loyalty", "Practicality"],
                "weaknesses": ["Possessiveness", "Stubbornness", "Materialism", "Resistance to change"],
                "compatibility": ["Virgo", "Capricorn", "Cancer"],
                "male": "The Taurus man is patient and sensual. He values stability and has strong determination.",
                "female": "The Taurus woman is grounded and nurturing. She appreciates beauty and creates comfortable surroundings."
            },
            "Gemini": {
                "date_range": "May 21 - June 20",
                "element": "Air",
                "ruling_planet": "Mercury",
                "traits": ["Curious", "Adaptable", "Social", "Witty", "Indecisive"],
                "strengths": ["Communication", "Adaptability", "Versatility", "Intellect"],
                "weaknesses": ["Inconsistency", "Nervousness", "Indecision", "Superficiality"],
                "compatibility": ["Libra", "Aquarius", "Aries"],
                "male": "The Gemini man is intellectually curious and communicative. He's versatile and always seeking new experiences.",
                "female": "The Gemini woman is quick-witted and sociable. She's mentally agile and enjoys diverse interactions."
            },
            "Cancer": {
                "date_range": "June 21 - July 22",
                "element": "Water",
                "ruling_planet": "Moon",
                "traits": ["Intuitive", "Emotional", "Protective", "Tenacious", "Moody"],
                "strengths": ["Empathy", "Loyalty", "Imagination", "Emotional depth"],
                "weaknesses": ["Moodiness", "Insecurity", "Manipulation", "Oversensitivity"],
                "compatibility": ["Scorpio", "Pisces", "Taurus"],
                "male": "The Cancer man is deeply intuitive and caring. He values family and creates a secure home environment.",
                "female": "The Cancer woman is nurturing and protective. She has strong intuition and deep emotional connections."
            },
            "Leo": {
                "date_range": "July 23 - August 22",
                "element": "Fire",
                "ruling_planet": "Sun",
                "traits": ["Generous", "Charismatic", "Creative", "Confident", "Dramatic"],
                "strengths": ["Leadership", "Warmth", "Creativity", "Loyalty"],
                "weaknesses": ["Arrogance", "Stubbornness", "Self-centeredness", "Inflexibility"],
                "compatibility": ["Aries", "Sagittarius", "Gemini"],
                "male": "The Leo man is confident and charismatic. He has natural leadership abilities and loves to be admired.",
                "female": "The Leo woman is passionate and creative. She has a regal presence and thrives on appreciation."
            },
            "Virgo": {
                "date_range": "August 23 - September 22",
                "element": "Earth",
                "ruling_planet": "Mercury",
                "traits": ["Analytical", "Detail-oriented", "Practical", "Reliable", "Critical"],
                "strengths": ["Precision", "Analysis", "Organization", "Helpfulness"],
                "weaknesses": ["Overthinking", "Criticality", "Perfectionism", "Worry"],
                "compatibility": ["Taurus", "Capricorn", "Cancer"],
                "male": "The Virgo man is methodical and analytical. He has high standards and pays attention to details.",
                "female": "The Virgo woman is practical and intelligent. She's observant and brings order to her surroundings."
            },
            "Libra": {
                "date_range": "September 23 - October 22",
                "element": "Air",
                "ruling_planet": "Venus",
                "traits": ["Diplomatic", "Fair", "Social", "Cooperative", "Indecisive"],
                "strengths": ["Diplomacy", "Fairness", "Partnership", "Charm"],
                "weaknesses": ["Indecision", "People-pleasing", "Avoidance", "Superficiality"],
                "compatibility": ["Gemini", "Aquarius", "Leo"],
                "male": "The Libra man is harmonious and balanced. He values partnerships and brings elegance to relationships.",
                "female": "The Libra woman is graceful and diplomatic. She seeks balance and has a natural sense of justice."
            },
            "Scorpio": {
                "date_range": "October 23 - November 21",
                "element": "Water",
                "ruling_planet": "Pluto, Mars",
                "traits": ["Passionate", "Resourceful", "Loyal", "Intense", "Secretive"],
                "strengths": ["Determination", "Passion", "Insight", "Magnetism"],
                "weaknesses": ["Jealousy", "Resentment", "Obsessiveness", "Suspicion"],
                "compatibility": ["Cancer", "Pisces", "Capricorn"],
                "male": "The Scorpio man is intense and perceptive. He has emotional depth and strong investigative abilities.",
                "female": "The Scorpio woman is magnetic and mysterious. She's deeply intuitive with transformative energy."
            },
            "Sagittarius": {
                "date_range": "November 22 - December 21",
                "element": "Fire",
                "ruling_planet": "Jupiter",
                "traits": ["Adventurous", "Optimistic", "Philosophical", "Open-minded", "Restless"],
                "strengths": ["Optimism", "Honesty", "Exploration", "Vision"],
                "weaknesses": ["Restlessness", "Bluntness", "Overcommitment", "Impatience"],
                "compatibility": ["Aries", "Leo", "Aquarius"],
                "male": "The Sagittarius man is adventurous and knowledge-seeking. He's honest and values freedom.",
                "female": "The Sagittarius woman is independent and enthusiastic. She has a philosophical outlook and loves exploration."
            },
            "Capricorn": {
                "date_range": "December 22 - January 19",
                "element": "Earth",
                "ruling_planet": "Saturn",
                "traits": ["Responsible", "Disciplined", "Self-controlled", "Ambitious", "Reserved"],
                "strengths": ["Discipline", "Responsibility", "Strategy", "Patience"],
                "weaknesses": ["Rigidity", "Pessimism", "Emotional distance", "Work addiction"],
                "compatibility": ["Taurus", "Virgo", "Scorpio"],
                "male": "The Capricorn man is ambitious and disciplined. He's responsible and works steadily toward goals.",
                "female": "The Capricorn woman is accomplished and pragmatic. She's persistent with strong management abilities."
            },
            "Aquarius": {
                "date_range": "January 20 - February 18",
                "element": "Air",
                "ruling_planet": "Uranus, Saturn",
                "traits": ["Independent", "Original", "Humanitarian", "Progressive", "Detached"],
                "strengths": ["Innovation", "Idealism", "Friendship", "Vision"],
                "weaknesses": ["Emotional detachment", "Stubbornness", "Unpredictability", "Extremism"],
                "compatibility": ["Gemini", "Libra", "Sagittarius"],
                "male": "The Aquarius man is innovative and intellectual. He's forward-thinking with humanitarian interests.",
                "female": "The Aquarius woman is unique and independent. She has original ideas and values personal freedom."
            },
            "Pisces": {
                "date_range": "February 19 - March 20",
                "element": "Water",
                "ruling_planet": "Neptune, Jupiter",
                "traits": ["Compassionate", "Artistic", "Intuitive", "Gentle", "Escapist"],
                "strengths": ["Empathy", "Creativity", "Intuition", "Compassion"],
                "weaknesses": ["Escapism", "Idealism", "Victim mentality", "Boundary issues"],
                "compatibility": ["Cancer", "Scorpio", "Capricorn"],
                "male": "The Pisces man is compassionate and artistic. He's deeply intuitive with a mystical perspective.",
                "female": "The Pisces woman is empathetic and imaginative. She's receptive to others with artistic sensibilities."
            }
        }

    def interpret(self, program_file):
        # Load the model
        model = zodiac_metamodel.model_from_file(program_file)
        # Execute the program
        return self.execute_program(model)

    def execute_program(self, program):
        for statement in program.statements:
            self.execute_statement(statement)
        return self.variables

    def execute_statement(self, statement):
        # Determine statement type and execute accordingly
        if hasattr(statement, 'name') and hasattr(statement, 'type') and hasattr(statement, 'expression'):
            # Variable declaration
            value = self.evaluate_expression(statement.expression) if hasattr(statement, 'expression') and statement.expression else None
            self.variables[statement.name] = value
        elif hasattr(statement, 'name') and hasattr(statement, 'prompt'):
            # Input statement
            self.variables[statement.name] = input(self.evaluate_expression(statement.prompt))
        elif hasattr(statement, 'expression') and hasattr(statement, 'thenBlock'):
            # If statement
            condition = self.evaluate_expression(statement.condition)
            if condition:
                self.execute_statement(statement.thenBlock)
            elif hasattr(statement, 'elseBlock'):
                self.execute_statement(statement.elseBlock)
        elif hasattr(statement, 'statements'):
            # Block
            for s in statement.statements:
                self.execute_statement(s)
        elif hasattr(statement, 'name') and hasattr(statement, 'params') and hasattr(statement, 'body'):
            # Function declaration
            self.functions[statement.name] = statement
        elif hasattr(statement, 'expression') and type(statement).__name__ == 'PrintStatement':
            # Print statement
            print(self.evaluate_expression(statement.expression))
        elif hasattr(statement, 'name') and hasattr(statement, 'args'):
            # Function call as a statement
            self.call_function(statement.name, statement.args)
        elif hasattr(statement, 'expression') and type(statement).__name__ == 'ReturnStatement':
            # Return statement
            self.return_value = self.evaluate_expression(statement.expression)
        else:
            raise Exception(f"Unknown statement type: {type(statement).__name__}")

    def evaluate_expression(self, expression):
        # Literal values
        if hasattr(expression, 'value'):
            return expression.value
        # Variable reference
        elif type(expression) == str:
            if expression in self.variables:
                return self.variables[expression]
            return expression
        # Function call as an expression
        elif hasattr(expression, 'name') and hasattr(expression, 'args'):
            return self.call_function(expression.name, expression.args)
        # Binary operation
        elif hasattr(expression, 'left') and hasattr(expression, 'operator') and hasattr(expression, 'right'):
            left = self.evaluate_expression(expression.left)
            right = self.evaluate_expression(expression.right)
            
            if expression.operator == '==':
                return left == right
            elif expression.operator == '!=':
                return left != right
            elif expression.operator == '<':
                return left < right
            elif expression.operator == '>':
                return left > right
            elif expression.operator == '<=':
                return left <= right
            elif expression.operator == '>=':
                return left >= right
            elif expression.operator == '+':
                return left + right
            elif expression.operator == '-':
                return left - right
            elif expression.operator == '*':
                return left * right
            elif expression.operator == '/':
                return left / right
            elif expression.operator == '&&':
                return left and right
            elif expression.operator == '||':
                return left or right
            else:
                raise Exception(f"Unknown operator: {expression.operator}")
        # Template string
        elif hasattr(expression, 'expression'):
            return str(self.evaluate_expression(expression.expression))
        else:
            return expression

    def call_function(self, name, args):
        # Built-in functions
        if name == 'getZodiac':
            birth_date = self.evaluate_expression(args[0])
            # Assuming birth_date is a string like "YYYY-MM-DD"
            try:
                date_parts = birth_date.split('-')
                if len(date_parts) != 3:
                    date_parts = birth_date.split('/')
                
                if len(date_parts) == 3:
                    year = int(date_parts[0])
                    month = int(date_parts[1])
                    day = int(date_parts[2])
                else:
                    # Try to handle alternative date formats
                    date_obj = datetime.datetime.strptime(birth_date, "%Y-%m-%d")
                    month = date_obj.month
                    day = date_obj.day
            except:
                # Default to a placeholder if date parsing fails
                return "Unknown"
            
            return self.get_zodiac_sign(month, day)
        
        elif name == 'generateReport':
            user_info = self.evaluate_expression(args[0])
            return self.generate_personality_report(user_info)
        
        elif name == 'collectUserInfo':
            first_name = input("First Name: ")
            last_name = input("Last Name: ")
            
            # Get birthdate
            birth_date = input("Birthdate (YYYY-MM-DD): ")
            
            # Get birth time
            birth_time = input("Birth Time (HH:MM, 24-hour format): ")
            
            # Get birth region
            birth_region = input("Birth Region/City: ")
            
            # Get gender
            gender = input("Gender (M/F): ").upper()
            
            # Return collected info as a dictionary
            return {
                "first_name": first_name,
                "last_name": last_name,
                "birth_date": birth_date,
                "birth_time": birth_time,
                "birth_region": birth_region,
                "gender": gender if gender in ["M", "F"] else "Unknown"
            }
        
        # User-defined functions
        elif name in self.functions:
            function = self.functions[name]
            
            # Create a new scope for function variables
            old_variables = self.variables.copy()
            
            # Set parameter values
            for i, param in enumerate(function.params):
                if i < len(args):
                    self.variables[param.name] = self.evaluate_expression(args[i])
                else:
                    self.variables[param.name] = None
            
            # Execute function body
            self.return_value = None
            self.execute_statement(function.body)
            
            # Restore original scope
            result = self.return_value
            self.variables = old_variables
            
            return result
        else:
            raise Exception(f"Unknown function: {name}")

    def get_zodiac_sign(self, month, day):
        if (month == 3 and day >= 21) or (month == 4 and day <= 19):
            return "Aries"
        elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
            return "Taurus"
        elif (month == 5 and day >= 21) or (month == 6 and day <= 20):
            return "Gemini"
        elif (month == 6 and day >= 21) or (month == 7 and day <= 22):
            return "Cancer"
        elif (month == 7 and day >= 23) or (month == 8 and day <= 22):
            return "Leo"
        elif (month == 8 and day >= 23) or (month == 9 and day <= 22):
            return "Virgo"
        elif (month == 9 and day >= 23) or (month == 10 and day <= 22):
            return "Libra"
        elif (month == 10 and day >= 23) or (month == 11 and day <= 21):
            return "Scorpio"
        elif (month == 11 and day >= 22) or (month == 12 and day <= 21):
            return "Sagittarius"
        elif (month == 12 and day >= 22) or (month == 1 and day <= 19):
            return "Capricorn"
        elif (month == 1 and day >= 20) or (month == 2 and day <= 18):
            return "Aquarius"
        else:
            return "Pisces"

    def generate_personality_report(self, user_info):
        try:
            # Extract date components
            date_parts = user_info["birth_date"].split('-')
            if len(date_parts) != 3:
                date_parts = user_info["birth_date"].split('/')
            
            if len(date_parts) == 3:
                year = int(date_parts[0])
                month = int(date_parts[1])
                day = int(date_parts[2])
            else:
                # Try to handle alternative date formats
                date_obj = datetime.datetime.strptime(user_info["birth_date"], "%Y-%m-%d")
                year = date_obj.year
                month = date_obj.month
                day = date_obj.day
                
            # Get the zodiac sign
            sign = self.get_zodiac_sign(month, day)
            
            # Get sign data
            sign_data = self.zodiac_data.get(sign, {})
            
            # Get gender-specific description
            gender_key = "female" if user_info.get("gender", "").upper() == "F" else "male"
            gender_description = sign_data.get(gender_key, "")
            
            # Format the report
            report = f"\n===== ZODIAC PERSONALITY REPORT =====\n\n"
            report += f"Name: {user_info.get('first_name', '')} {user_info.get('last_name', '')}\n"
            report += f"Date of Birth: {user_info.get('birth_date', '')}\n"
            report += f"Time of Birth: {user_info.get('birth_time', '')}\n"
            report += f"Region: {user_info.get('birth_region', '')}\n\n"
            
            report += f"Your Zodiac Sign is: {sign}\n"
            report += f"Date Range: {sign_data.get('date_range', '')}\n"
            report += f"Element: {sign_data.get('element', '')}\n"
            report += f"Ruling Planet: {sign_data.get('ruling_planet', '')}\n\n"
            
            report += "Key Traits:\n"
            for trait in sign_data.get('traits', []):
                report += f"- {trait}\n"
            
            report += "\nStrengths:\n"
            for strength in sign_data.get('strengths', []):
                report += f"- {strength}\n"
            
            report += "\nWeaknesses:\n"
            for weakness in sign_data.get('weaknesses', []):
                report += f"- {weakness}\n"
            
            report += f"\nBest Compatibility: {', '.join(sign_data.get('compatibility', []))}\n\n"
            
            report += f"Personal Insight: {gender_description}\n\n"
            
            report += "===============================\n"
            
            return report
        except Exception as e:
            return f"Unable to generate report: {str(e)}"

# Main execution function for the interpreter
def run_zodiac_program(file_path):
    interpreter = ZodiacInterpreter()
    result = interpreter.interpret(file_path)
    return result

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        file_path = sys.argv[1]
        run_zodiac_program(file_path)
    else:
        print("Please provide a Zodiac program file path.")