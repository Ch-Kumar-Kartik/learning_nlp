# Shakespeare Play Excerpts Dataset
# Each play contains a representative excerpt for TF-IDF analysis

shakespeare_plays = {
    "Hamlet": """
        To be, or not to be, that is the question:
        Whether 'tis nobler in the mind to suffer
        The slings and arrows of outrageous fortune,
        Or to take arms against a sea of troubles
        And by opposing end them. To die—to sleep,
        No more; and by a sleep to say we end
        The heart-ache and the thousand natural shocks
        That flesh is heir to: 'tis a consummation
        Devoutly to be wish'd. To die, to sleep;
        To sleep, perchance to dream—ay, there's the rub:
        For in that sleep of death what dreams may come,
        When we have shuffled off this mortal coil,
        Must give us pause—there's the respect
        That makes calamity of so long life.
    """,
    
    "Romeo and Juliet": """
        But soft, what light through yonder window breaks?
        It is the East, and Juliet is the sun!
        Arise, fair sun, and kill the envious moon,
        Who is already sick and pale with grief
        That thou her maid art far more fair than she.
        O Romeo, Romeo, wherefore art thou Romeo?
        Deny thy father and refuse thy name,
        Or if thou wilt not, be but sworn my love
        And I'll no longer be a Capulet.
        What's in a name? That which we call a rose
        By any other name would smell as sweet.
    """,
    
    "Macbeth": """
        Tomorrow, and tomorrow, and tomorrow,
        Creeps in this petty pace from day to day,
        To the last syllable of recorded time;
        And all our yesterdays have lighted fools
        The way to dusty death. Out, out, brief candle!
        Life's but a walking shadow, a poor player,
        That struts and frets his hour upon the stage,
        And then is heard no more. It is a tale
        Told by an idiot, full of sound and fury,
        Signifying nothing. Fair is foul, and foul is fair,
        Hover through the fog and filthy air.
    """,
    
    "Julius Caesar": """
        Friends, Romans, countrymen, lend me your ears!
        I come to bury Caesar, not to praise him.
        The evil that men do lives after them;
        The good is oft interred with their bones.
        So let it be with Caesar. The noble Brutus
        Hath told you Caesar was ambitious.
        If it were so, it was a grievous fault,
        And grievously hath Caesar answered it.
        Beware the ides of March. Et tu, Brute?
        Then fall Caesar! Cowards die many times before their deaths;
        The valiant never taste of death but once.
    """,
    
    "Othello": """
        O, beware, my lord, of jealousy!
        It is the green-eyed monster which doth mock
        The meat it feeds on. That cuckold lives in bliss
        Who, certain of his fate, loves not his wronger;
        But O, what damned minutes tells he o'er
        Who dotes, yet doubts; suspects, yet strongly loves!
        I kissed thee ere I killed thee. No way but this,
        Killing myself, to die upon a kiss.
        Reputation, reputation, reputation! O, I have lost my reputation!
    """,
    
    "A Midsummer Night's Dream": """
        The course of true love never did run smooth.
        Lord, what fools these mortals be!
        I know a bank where the wild thyme blows,
        Where oxlips and the nodding violet grows,
        Quite over-canopied with luscious woodbine,
        With sweet musk-roses and with eglantine.
        Love looks not with the eyes, but with the mind,
        And therefore is winged Cupid painted blind.
        The lunatic, the lover, and the poet
        Are of imagination all compact.
    """,
    
    "The Tempest": """
        We are such stuff as dreams are made on,
        And our little life is rounded with a sleep.
        Full fathom five thy father lies;
        Of his bones are coral made;
        Those are pearls that were his eyes:
        Nothing of him that doth fade,
        But doth suffer a sea-change
        Into something rich and strange.
        O brave new world, that has such people in it!
        Hell is empty and all the devils are here.
    """,
    
    "King Lear": """
        How sharper than a serpent's tooth it is
        To have a thankless child! Blow, winds, and crack your cheeks!
        Rage, blow, you cataracts and hurricanoes!
        Nothing will come of nothing. Speak again.
        As flies to wanton boys are we to the gods;
        They kill us for their sport. I am a man
        More sinned against than sinning. Thou art thy mother's glass,
        and she in thee calls back the lovely April of her prime.
    """,
    
    "Much Ado About Nothing": """
        Sigh no more, ladies, sigh no more,
        Men were deceivers ever,
        One foot in sea and one on shore,
        To one thing constant never.
        Some Cupid kills with arrows, some with traps.
        In time the savage bull doth bear the yoke.
        Everyone can master a grief but he that has it.
        When I said I would die a bachelor, I did not think I should live till I were married.
    """,
    
    "The Merchant of Venice": """
        The quality of mercy is not strained.
        It droppeth as the gentle rain from heaven
        Upon the place beneath. It is twice blessed:
        It blesseth him that gives and him that takes.
        All that glisters is not gold;
        Often have you heard that told.
        If you prick us, do we not bleed?
        If you tickle us, do we not laugh?
        If you poison us, do we not die?
        And if you wrong us, shall we not revenge?
    """
}

# Sample queries for testing
sample_queries = [
    "love marriage romance",
    "death mortality grief",
    "revenge murder betrayal",
    "power ambition kingdom",
    "jealousy envy green-eyed monster"
]
