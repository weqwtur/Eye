from aiogram import Router, F
from aiogram.types import Message, CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
import random

router = Router()

EYE_FACTS = [
    {
        "text": "The six muscles in each of your eyes move faster than any other muscles in your body. Your brain uses these zippy muscles to control eye movement through three cranial nerves.",
        "source": "https://health.clevelandclinic.org/eye-facts"
    },
    {
        "text": "Your eyes grow along with the rest of your body during childhood. They get considerably larger in your first two years of life and then experience another growth spurt during puberty. Eyes typically reach full size in early adulthood.",
        "source": "https://health.clevelandclinic.org/eye-facts"
    },
    {
        "text": "Human eyes typically end up about 24 millimeters (mm) wide. That's slightly less than an inch for those more familiar with the Imperial system of measurement.",
        "source": "https://health.clevelandclinic.org/eye-facts"
    },
    {
        "text": "For comparison's sake, the largest eyes among land animals belong to the ostrich and are about 50 mm (or 2 inches) in diameter. The largest eyes at sea belong to the giant squid and are about the size of a dinner plate.",
        "source": "https://health.clevelandclinic.org/eye-facts"
    },
    {
        "text": "When the lenses in your eyes focus an image on your retina, it's upside down and backward. Your brain reorients and right-sizes the image for you while 'developing' what you see.",
        "source": "https://health.clevelandclinic.org/eye-facts"
    },
    {
        "text": "Seven million photoreceptor cone cells in your retina bring you the world in living color. Your brain can interpret an estimated 10 million different colors. No wonder why we have so many paint options!",
        "source": "https://health.clevelandclinic.org/eye-facts"
    },
    {
        "text": "Despite being able to see so many different colors, cone cells only detect three — red, green and blue. Your brain combines signals from that trio to show you a full rainbow of hues.",
        "source": "https://health.clevelandclinic.org/eye-facts"
    },
    {
        "text": "Color blindness occurs when certain color-detecting cones are missing. Around 300 million people around the world have some form of color blindness. Men are more likely to be color blind.",
        "source": "https://health.clevelandclinic.org/eye-facts"
    },
    {
        "text": "Your retina is also home to more than 100 million photoreceptor rods that help you see in dark and dim conditions. Rods are extremely sensitive and respond to even a few photons of light.",
        "source": "https://health.clevelandclinic.org/eye-facts"
    },
    {
        "text": "Photoreceptor rods don't assist with color vision but they do help you see up to 500 different shades of gray.",
        "source": "https://health.clevelandclinic.org/eye-facts"
    },
    {
        "text": "Babies are born with blurred vision that gradually improves during their first few months in the world. It takes about four months for an infant to fully see colors and distant objects.",
        "source": "https://health.clevelandclinic.org/eye-facts"
    },
    {
        "text": "Ever notice how a baby's eyes might suddenly cross or even seem out of synch? These unusual movements are common as a newborn's vision develops and they learn how to focus.",
        "source": "https://health.clevelandclinic.org/eye-facts"
    },
    {
        "text": "Tears are less common at the beginning and the end of life. Newborns don't start producing tears until they're between 1 and 3 months old. The older you get, the fewer tears you produce.",
        "source": "https://health.clevelandclinic.org/eye-facts"
    },
    {
        "text": "The color of your eyes is as unique as your fingerprints, with no two people sharing the same hue. Shades of brown are the most common color. Variations of green are the rarest.",
        "source": "https://health.clevelandclinic.org/eye-facts"
    },
    {
        "text": "Eye color doesn't typically change after your first year of life. If it does switch, it could be a sign of an issue that deserves attention from an eye doctor.",
        "source": "https://health.clevelandclinic.org/eye-facts"
    },
    {
        "text": "Smoking and secondhand smoke increase your risk for cataracts, macular degeneration and other issues that could cost you your vision.",
        "source": "https://health.clevelandclinic.org/eye-facts"
    },
    {
        "text": "Having two eyes helps with depth perception. Your brain computes distances by comparing the distinct images from each eye.",
        "source": "https://health.clevelandclinic.org/eye-facts"
    },
    {
        "text": "A vision change may signal the emergence of larger health issues like diabetes, high blood pressure or various inflammatory diseases.",
        "source": "https://health.clevelandclinic.org/eye-facts"
    },
    {
        "text": "Sunglasses aren't just an expression of style. They're a way to keep your eyes healthy by blocking harmful ultraviolet (UV) sunlight that can harm your vision over time. Your risk of sun-related damage is higher if your eyes are lighter in color.",
        "source": "https://health.clevelandclinic.org/eye-facts"
    },
    {
        "text": "Blinking is a basic reflex to protect your eyes. On average, adults blink about 14 to 17 times a minute. That adds up to between 13,440 and 16,320 blinks a day if you're awake for 16 hours.",
        "source": "https://health.clevelandclinic.org/eye-facts"
    },
    {
        "text": "The human eye works just like a camera. In the same way that a camera lens focuses light onto a photosensitive surface, your eyes focus light onto the retina.",
        "source": "https://www.lenstore.co.uk/eyecare/51-human-eye-facts"
    },
    {
        "text": "Eyes first evolved around 500 million years ago. Scientists estimate that eyes first evolved 500 million years ago, originally in a very simple form that could probably only distinguish light from dark.",
        "source": "https://www.lenstore.co.uk/eyecare/51-human-eye-facts"
    },
    {
        "text": "The most common eye colour in the world is brown. With over 55% of the world's population having brown eyes, it remains the most common colour. Eye colour is determined by genetics, because they dictate how much melanin is produced in your iris.",
        "source": "https://www.lenstore.co.uk/eyecare/51-human-eye-facts"
    },
    {
        "text": "Some people are born with mismatched eye colours. This condition is known as heterochromia, and is usually the result of a relative lack or excess of pigment in one eye. It is most often inherited, but may also occur due to disease or injury.",
        "source": "https://www.lenstore.co.uk/eyecare/51-human-eye-facts"
    },
    {
        "text": "The cornea is the transparent covering of the iris and pupil. It protects your eyes from dirt and germs, as well as some of the sun's UV rays. If your cornea becomes damaged you will experience distorted vision.",
        "source": "https://www.lenstore.co.uk/eyecare/51-human-eye-facts"
    },
    {
        "text": "20/20 vision just means you have normal eyesight. Contrary to popular belief, having 20/20 vision isn't anything remarkable. Rather, it means that you can read a chart from 20 feet away in normal lighting conditions.",
        "source": "https://www.lenstore.co.uk/eyecare/51-human-eye-facts"
    },
    {
        "text": "Wider pupils can suggest excitement. Any positive thought can serve to dilate your pupils. For example, when you look at someone you are attracted to, they will expand up to 45%. However, dilating pupils can also mean you are scared.",
        "source": "https://www.lenstore.co.uk/eyecare/51-human-eye-facts"
    },
    {
        "text": "It's a myth that liars make less eye contact. In fact, a well-practised liar will try to overcompensate as an attempt to 'prove' they are telling the truth, by making too much eye contact and holding a gaze.",
        "source": "https://www.lenstore.co.uk/eyecare/51-human-eye-facts"
    },
    {
        "text": "A woman's eyesight can be affected by pregnancy. While hormones are raging and physical changes are occurring, it is possible for a woman to experience problems with her sight. These are usually minor and temporary conditions such as blurred vision and dry eyes.",
        "source": "https://www.lenstore.co.uk/eyecare/51-human-eye-facts"
    },
    {
        "text": "Your eyes become tired when you read or stare at a computer for extended periods of time. This is because you blink less often and you are not relaxing the muscle inside your eye. If this happens to you often, you should make sure that you have an up-to-date prescription.",
        "source": "https://www.lenstore.co.uk/eyecare/51-human-eye-facts"
    },
    {
        "text": "Human corneas are very similar to a sharks' cornea. This similarity means that sharks' eyes can be used as replacements in human eye surgeries.",
        "source": "https://www.lenstore.co.uk/eyecare/51-human-eye-facts"
    },
    {
        "text": "The 'floaters' in your vision are permanent. They are mainly made up of protein strands floating inside the eye's vitreous, casting shadows on the retina. Because the vitreous is completely stagnant, they will remain there indefinitely unless surgically removed.",
        "source": "https://www.lenstore.co.uk/eyecare/51-human-eye-facts"
    },
    {
        "text": "It's impossible to sneeze with your eyes open. Your eyes and nose are connected by cranial nerves, so the stimulation from a sneeze travels up one nerve to the brain, then down another nerve to the eyelids, typically prompting a blink.",
        "source": "https://www.lenstore.co.uk/eyecare/51-human-eye-facts"
    },
    {
        "text": "Smokers have almost double the chance of experiencing dry eye. Tobacco smoke is known to irritate eyes - even second hand exposure to the smoke can worsen dry eye, particularly for contact lens wearers.",
        "source": "https://www.lenstore.co.uk/eyecare/51-human-eye-facts"
    },
    {
        "text": "The sun's rays have been linked to eye damage. Several eye conditions, such as cataracts and pterygia, have been associated with exposure to UV rays. To protect your eyes from the dangers of the sun, you should wear well fitted sunglasses.",
        "source": "https://www.lenstore.co.uk/eyecare/51-human-eye-facts"
    },
    {
        "text": "Many eye injuries are surprisingly quick to heal. Our bodies understand that our eyes are very important to us, and many eye injuries can be recovered from very quickly. For example, with the correct care, a minor corneal scratch will heal in around 2 days.",
        "source": "https://www.lenstore.co.uk/eyecare/51-human-eye-facts"
    },
    {
        "text": "While a fingerprint has 40 unique characteristics, an iris has 256. This is why retinal scans are increasingly being used for security purposes. A retinal scanner uses infrared light to map the unique pattern of blood vessels on a person's retina.",
        "source": "https://www.lenstore.co.uk/eyecare/51-human-eye-facts"
    },
    {
        "text": "We have two eyeballs for depth perception. Our eyes work together to help us judge the size and distance of objects, so that we can safely navigate around them.",
        "source": "https://www.lenstore.co.uk/eyecare/51-human-eye-facts"
    },
    {
        "text": "Tears help protect our eyes from infection. Any dirt and dust that has managed to pass the defence of our eyelashes and brows is washed away by tears. They keep our eyes clean and moist and filled with antibodies that fight infection.",
        "source": "https://www.lenstore.co.uk/eyecare/51-human-eye-facts"
    },
    {
        "text": "Our eyes close automatically to protect us from perceived dangers. The superb reflex control of our eyelids allows them close automatically when they detect that an object is too close to the eye or there is sudden bright light.",
        "source": "https://www.lenstore.co.uk/eyecare/51-human-eye-facts"
    },
    {
        "text": "We actually see things upside down and our brain turns the image the correct way up. As a result of having a curved cornea, the light that enters our eyes is refracted and creates an upside down image on the retina.",
        "source": "https://www.lenstore.co.uk/eyecare/51-human-eye-facts"
    },
    {
        "text": "There are colours that are too complex for the human eye to comprehend. These are known as 'impossible colours', which cannot be perceived due to being outside the strength of our three types of cone cell in the retina.",
        "source": "https://www.lenstore.co.uk/eyecare/51-human-eye-facts"
    },
    {
        "text": "Eye transplants are currently impossible due to the sensitivity of the optic nerve. Surgeons are currently unable to wire the optic nerve to the brain because it contains over 1 million nerve cells. A transplanted eye would not transmit signals to the brain.",
        "source": "https://www.lenstore.co.uk/eyecare/51-human-eye-facts"
    },
    {
        "text": "You should throw away your eye makeup after three months. Creamy or liquid eye makeup, such as mascara, is the perfect breeding ground for bacteria. This can cause eye infections.",
        "source": "https://www.lenstore.co.uk/eyecare/51-human-eye-facts"
    },
    {
        "text": "You should never share eye makeup with friends. Swapping your eye makeup can lead to nasty infections. This is because makeup applicators can easily carry bacteria and you don't want to trade germs with others.",
        "source": "https://www.lenstore.co.uk/eyecare/51-human-eye-facts"
    },
    {
        "text": "Eye tests can detect Schizophrenia. The mental disorder can be diagnosed with 98.3% precision using a simple examination of the eyes. The test checks for abnormalities of eye movement.",
        "source": "https://www.lenstore.co.uk/eyecare/51-human-eye-facts"
    },
    {
        "text": "The cornea is the only tissue in the human body which doesn't contain blood vessels. The cornea must remain clear in order to refract light correctly. If blood vessels were present, they would interfere with this process.",
        "source": "https://www.lenstore.co.uk/eyecare/51-human-eye-facts"
    },
    {
        "text": "In space, an astronaut cannot cry. Due to the lack of gravity in space, tears do not fall. Instead they collect in little balls and make a person's eyes sting.",
        "source": "https://www.lenstore.co.uk/eyecare/51-human-eye-facts"
    },
    {
        "text": "Astigmatism refers to a curvature of the cornea or lens. It is a common and usually not a serious problem. It causes distorted vision and toric lenses are prescribed to aid the individual's sight.",
        "source": "https://www.lenstore.co.uk/eyecare/51-human-eye-facts"
    },
    {
        "text": "Just behind our pupil is the lens - which is round, flat and thicker toward the middle. It is made of transparent, flexible tissue and, together with the cornea, helps to focus light onto the retina.",
        "source": "https://www.lenstore.co.uk/eyecare/51-human-eye-facts"
    },
    {
        "text": "Part of the retina is insensitive to light. Human eyes contain a small blind spot, known as the Punctum Caecum. It is rarely noticed because our brains are able to use information from the other eye to fill in the vision gap.",
        "source": "https://www.lenstore.co.uk/eyecare/51-human-eye-facts"
    },
    {
        "text": "Diabetes affects the blood vessels of your eyes. If these blood vessels become blocked or leak then the retina, and perhaps your vision, will be harmed. This is called Diabetic Retinopathy and affects 40% of people with Type 1 diabetes and 20% with Type 2 diabetes.",
        "source": "https://www.lenstore.co.uk/eyecare/51-human-eye-facts"
    },
    {
        "text": "Diabetes is usually first detected during an eye test. Sufferers of type 2 diabetes often have no noticeable symptoms. If this is the case, then the condition is often first noticed during eye examinations due to tiny haemorrhages leaking from blood vessels.",
        "source": "https://www.lenstore.co.uk/eyecare/51-human-eye-facts"
    },
    {
        "text": "You blink on average 4,200,000 times a year. The purpose of blinking is to lubricate the eyes. Adults blink around 15 - 20 times a minute, which researchers say is more than the required amount to keep the eyes moist.",
        "source": "https://www.lenstore.co.uk/eyecare/51-human-eye-facts"
    },
    {
        "text": "Babies blink a lot less than adults. There are several theories as to why babies only blink one or two times a minute. Some researchers believe that it is because a baby's eye-opening is much smaller and therefore requires less lubrication.",
        "source": "https://www.lenstore.co.uk/eyecare/51-human-eye-facts"
    },
    {
        "text": "Oily fish, vitamin A and vitamin C all help to preserve good eyesight. Eating oily fish at least twice a week can help reduce the risk of age-related macular degeneration - a common cause of blindness in old age.",
        "source": "https://www.lenstore.co.uk/eyecare/51-human-eye-facts"
    },
    {
        "text": "On average, people are likely to look at each other between one and seven seconds before looking away. Constant eye contact can be intimidating and unpleasant for the other person. When listening to someone else, it is good to maintain eye contact 90% of the time.",
        "source": "https://www.lenstore.co.uk/eyecare/51-human-eye-facts"
    },
    {
        "text": "Your eye is the fastest reacting muscle in your body. It contracts in less than 1/100th of a second. The eye muscles collaboratively carry out a total of seven corresponding movements that allow you to trail moving objects.",
        "source": "https://www.lenstore.co.uk/eyecare/51-human-eye-facts"
    },
    {
        "text": "Around 99% of the world's population will first need reading glasses between the ages of 43 and 50. As we age, the lenses in our eyes slowly lose the ability to focus. This means that the vast majority of us will need some form of vision correction.",
        "source": "https://www.lenstore.co.uk/eyecare/51-human-eye-facts"
    },
    {
        "text": "Cleaning your contact lenses with water will do more harm than good. Never try and clean your contact lenses with water, whether it is bottled or from the tap. This can lead to serious eye infections.",
        "source": "https://www.lenstore.co.uk/eyecare/51-human-eye-facts"
    },
    {
        "text": "Your eyes contain 7 million cones which help you see colour and detail, as well as 100 million cells called rods which help you see better in the dark. In order to work well, cones need more light than rods. Rods cannot perceive colour, just black, white and gray.",
        "source": "https://www.lenstore.co.uk/eyecare/51-human-eye-facts"
    },
    {
        "text": "The human eye only sees three colours. The retina has three types of cones; one is sensitive to the colour red, one is sensitive to the colour blue and the other is sensitive to the colour green. These three cones work together to sense combinations of light waves.",
        "source": "https://www.lenstore.co.uk/eyecare/51-human-eye-facts"
    },
    {
        "text": "Flitting eyes suggest distress or tension. Sometimes, when a person's eyes are darting around, it is because they are trying to find a solution or an answer in a difficult situation.",
        "source": "https://www.lenstore.co.uk/eyecare/51-human-eye-facts"
    },
    {
        "text": "Anisocoria is a condition where a person's pupils are not the same size. It can be present at birth or can be developed over time, however it is very rare. Sometimes, people with this condition will notice that the difference in size is only temporary.",
        "source": "https://www.lenstore.co.uk/eyecare/51-human-eye-facts"
    },
    {
        "text": "Red-green colour blindness is primarily found in men. The genes for the red and green colour receptors are found on the X chromosome, of which men only have one. Women, on the other hand, have two X chromosomes and the stronger of the two is superior.",
        "source": "https://www.lenstore.co.uk/eyecare/51-human-eye-facts"
    },
    {
        "text": "Your eyes start to develop just two weeks after conception. This is one of the reasons why it is so important for a pregnant woman to take care of her own body so that her unborn child can develop properly.",
        "source": "https://www.lenstore.co.uk/eyecare/51-human-eye-facts"
    },
    {
        "text": "At birth, babies can only see in black, white and some shades of gray. This is because certain nerve cells in their retina and brain are not fully developed. However, they develop the ability to see in colour as quickly as a week later.",
        "source": "https://www.lenstore.co.uk/eyecare/51-human-eye-facts"
    },
    {
        "text": "People with blue-eyes share the same ancestor. Originally, all human beings had brown eyes, until a genetic mutation occurred between 6,000 and 10,000 years ago. Every single blue-eyed person shares this very distant relative.",
        "source": "https://www.lenstore.co.uk/eyecare/51-human-eye-facts"
    },
    {
        "text": "Male and female brains process colours slightly differently. Research has shown that men and women see colours slightly differently. It is likely that the male hormone, testosterone, affects the way a male brain processes information taken in by the eye.",
        "source": "https://www.lenstore.co.uk/eyecare/51-human-eye-facts"
    },
    {
        "text": "Red-eye in photos is caused by light from the flash bouncing off the capillaries in people's eyes. When camera flash is used at night, or in dim lighting, it can reflect from the subject's retina and show up on the picture as red eye.",
        "source": "https://www.lenstore.co.uk/eyecare/51-human-eye-facts"
    },
    {
        "text": "Playing Tetris can treat a lazy-eye. Canadian doctors have found that the puzzle game is effective in training both eyes to work together. In fact, it works better than the conventional eye patch.",
        "source": "https://www.lenstore.co.uk/eyecare/51-human-eye-facts"
    },
    {
        "text": "Your eyes are comprised of over 2 million working parts to make them fully functional.",
        "source": "https://performanceeyecare.com/25-fun-and-interesting-facts-you-didnt-know-about-your-eyes/"
    },
    {
        "text": "The most active muscles in your entire body are the muscles that control the eyes.",
        "source": "https://performanceeyecare.com/25-fun-and-interesting-facts-you-didnt-know-about-your-eyes/"
    },
    {
        "text": "Eyes can process about 36,000 bits of information each hour.",
        "source": "https://performanceeyecare.com/25-fun-and-interesting-facts-you-didnt-know-about-your-eyes/"
    },
    {
        "text": "Our eyes are approximately 1 inch across and weigh about 1/4 of an ounce.",
        "source": "https://performanceeyecare.com/25-fun-and-interesting-facts-you-didnt-know-about-your-eyes/"
    },
    {
        "text": "An eye blinks over 10,000,000 times in ONE YEAR!",
        "source": "https://performanceeyecare.com/25-fun-and-interesting-facts-you-didnt-know-about-your-eyes/"
    },
    {
        "text": "Our eyes can distinguish between 500 shades of gray.",
        "source": "https://performanceeyecare.com/25-fun-and-interesting-facts-you-didnt-know-about-your-eyes/"
    },
    {
        "text": "Your pupils change in size in order to allow different amounts of light into the eyes.",
        "source": "https://performanceeyecare.com/25-fun-and-interesting-facts-you-didnt-know-about-your-eyes/"
    },
    {
        "text": "Your eyes always remain the same size once you are born, but your ears and nose will never stop growing.",
        "source": "https://performanceeyecare.com/25-fun-and-interesting-facts-you-didnt-know-about-your-eyes/"
    },
    {
        "text": "Those who are blind can see their dreams as long as they weren't born blind.",
        "source": "https://performanceeyecare.com/25-fun-and-interesting-facts-you-didnt-know-about-your-eyes/"
    },
    {
        "text": "Your eyes use about 65% of your brainpower, the most out of ANY body part!",
        "source": "https://performanceeyecare.com/25-fun-and-interesting-facts-you-didnt-know-about-your-eyes/"
    },
    {
        "text": "Some people are born with two differently colored eyes. This condition is known as heterochromia. For example, pitcher Max Scherzer of the Detroit Tigers has a brown eye and a blue eye!",
        "source": "https://performanceeyecare.com/25-fun-and-interesting-facts-you-didnt-know-about-your-eyes/"
    },
    {
        "text": "Each eyelash has a life span of approximately 5 months.",
        "source": "https://performanceeyecare.com/25-fun-and-interesting-facts-you-didnt-know-about-your-eyes/"
    },
    {
        "text": "It may take time for most of your body to warm up to their full potential every day, but your eyes are ALWAYS on their 'A game!'",
        "source": "https://performanceeyecare.com/25-fun-and-interesting-facts-you-didnt-know-about-your-eyes/"
    },
    {
        "text": "Pirates used to wear a gold earring because they believed it would improve their eyesight.",
        "source": "https://performanceeyecare.com/25-fun-and-interesting-facts-you-didnt-know-about-your-eyes/"
    },
    {
        "text": "Doctors have yet to find a way to transplant an eyeball successfully. The optic nerve that connects the eye to the brain is too delicate to successfully reconstruct.",
        "source": "https://performanceeyecare.com/25-fun-and-interesting-facts-you-didnt-know-about-your-eyes/"
    },
    {
        "text": "The leading cause of blindness in the United States is diabetes.",
        "source": "https://performanceeyecare.com/25-fun-and-interesting-facts-you-didnt-know-about-your-eyes/"
    },
]

random.shuffle(EYE_FACTS)


def get_keyboard(current_index: int, total_facts: int, show_back: bool = False) -> InlineKeyboardMarkup:
    buttons = []
    
    prev_index = current_index - 1
    next_index = current_index + 1
    
    row = []
    if current_index > 0:
        row.append(InlineKeyboardButton(text="⬅", callback_data=f"fact_{prev_index}"))
        
    if current_index < total_facts - 1:
        row.append(InlineKeyboardButton(text="⭢", callback_data=f"fact_{next_index}"))
        
    if row:
        buttons.append(row)
    
    if show_back:
        buttons.append([InlineKeyboardButton(text="⬅ Back to Menu", callback_data="menu:back")])
        
    return InlineKeyboardMarkup(inline_keyboard=buttons)


def format_fact_message(fact_index: int) -> str:
    fact = EYE_FACTS[fact_index]
    total = len(EYE_FACTS)
    return (
        f"<b>Fact #{fact_index + 1}</b> (of {total})\n\n"
        f"<i>{fact['text']}</i>\n\n"
        f"<b>From:</b> <a href=\"{fact['source']}\">Source</a>"
    )


async def cmd_facts(message: Message):
    """Called from menu callback - edits the existing message"""
    text = format_fact_message(0)
    keyboard = get_keyboard(0, len(EYE_FACTS), show_back=True)
    await message.edit_text(text=text, reply_markup=keyboard, parse_mode="HTML", disable_web_page_preview=True)


@router.callback_query(F.data.startswith("fact_"), F.message.chat.type == "private")
async def turn_fact_page(callback: CallbackQuery):
    target_index = int(callback.data.split("_")[1])
    total_facts = len(EYE_FACTS)
    
    text = format_fact_message(target_index)
    keyboard = get_keyboard(target_index, total_facts, show_back=True)
    
    try:
        await callback.message.edit_text(
            text=text, 
            reply_markup=keyboard, 
            parse_mode="HTML",
            disable_web_page_preview=True
        )
    except Exception:
        pass
        
    await callback.answer()





