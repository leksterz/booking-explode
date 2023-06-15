# booking-explode
EXPLODE BOOKING 
Documentation

**Background:**
Explode Booking is a Django web application designed to simplify and automate the booking process for music recording studios. The application allows artists to view studio availability, book sessions with engineers, and receive notifications about their booking status. Studio owners and engineers can manage bookings and approve or reject requests.

The following documentation captures the building blocks of the project from a technical capability perspective. The language is aimed to be consumed by programmers and non-programmers alike.

**Data and models:**
In a Django application, models are like folders in a big cabinet that help you organize everything about your recording studio. Each folder (model) has a label that tells you what type of information belongs inside (like recording engineers, artists, or bookings). We use models to store and organize different pieces of information about the recording studio. Just like with folders, these models help us find what we're looking for more easily and keep everything in order.

Now, sometimes one folder needs to know what's inside another folder. For example, a booking might be related to a specific artist and a specific engineer. So we connect the booking folder to the artist folder and the engineer folder to show that they go together. By connecting these folders (models), we can easily find out which engineer an artist is working with or which artists an engineer has helped. These connections between folders (models) make our Django app even more organized and help us find the information we need quickly and easily.

We will be using the following models:
1. Studio: This model represents the recording studios, like Studio A and Studio B. Each studio has a name (such as "Studio A") and a location (like "Brooklyn, NY").
2. Engineer: This model is for the people who help artists record their music. They are called recording engineers. Each engineer has a name (like "John") and working hours (like "12 PM to 7 PM").
3. Artist: This model represents the musicians or singers who come to the studio to make music. Each artist has a name (like "Alice") and contact information (like their phone number or email address).
4. Booking: This model is for when an artist wants to use a studio with a specific engineer for a certain amount of time. A booking has information about which studio it is for, which engineer will help the artist, which artist made the booking, the time when the booking starts and ends (like "3 PM to 5 PM"), and the status of the booking (like "pending," "accepted," or "declined").

