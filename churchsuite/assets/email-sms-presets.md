# Preset wording

Use merge fields from the editor. Keep one clear ask per message.

## Welcome newcomer (email)
Subject: Great to meet you, ::first_name::
Body: Hi ::first_name::, it was lovely to meet you on Sunday. Here is what is happening this week: [one line]. Reply to this email if you have any questions. [Name], [Church]

## Rota reminder (email)
Subject: You are serving on ::serving_date::
Body: Hi ::first_name::, thank you for serving as ::roles:: on ::serving_date::. If you can no longer make it, please arrange a swap in My ChurchSuite as soon as you can.

## Event reminder (SMS)
Hi ::first_name::, a reminder that [event] is on [day] at [time] at [place]. [Church]

## Group welcome (email)
Subject: Welcome to [group]
Body: Hi ::first_name::, we meet on [day] at [time] at [place]. Your leader is [name]. Looking forward to seeing you.

Check merge field names against your account before using. Names above are placeholders, confirm in the editor. Run scripts/merge_field_lint.py on any draft.
