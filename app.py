from flask import Flask, redirect, render_template, request, flash
from flask_mail import Mail, Message
from pytube import YouTube
import random

app = Flask(__name__)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = 'ry360596@gmail.com'
app.config['MAIL_PASSWORD'] = 'nxqz cvrn nxwi ujxh'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False

mail = Mail(app)

app.secret_key = "Youtube Downloader"

user_url = ""
correct_answer = random.randint(1, 100)
remaining_points = 6


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/search', methods=['GET', 'POST'])
def Search():
    global user_url
    if request.method == 'POST':
        user_url = request.form['user_url']
        yt = YouTube(user_url)
        title = yt.title
        return render_template('index.html', title=title, user_url=user_url)
    

@app.route('/about')
def About():
    return render_template('about.html')


@app.route('/guessinggame', methods=['GET', 'POST'])
def Games():
    global correct_answer, remaining_points
    if request.method == 'POST':
        try:
            guessed_number = int(request.form['guessedNumber'])
            if remaining_points == 1:
                if correct_answer == guessed_number:
                    flash(f"Congratulations! You've Guessed it right! The secret Number is: {correct_answer}. Your Mind is Blowing Bro 🎉🎉", 'right')
                    print(correct_answer)
                    remaining_points = 6
                    correct_answer = random.randint(1, 100)
                    print(correct_answer)
                else:
                    flash(f"Game Over Sorry, you've run out of Chances. The correct Number is: {correct_answer} Better luck next time!", 'lose')
                    remaining_points = 6
                    correct_answer = random.randint(1, 100)
                    return render_template('guessing.html', point=remaining_points)
            elif guessed_number < 1 or guessed_number > 100:
                flash("Please Enter a Number Between 1 and 100", 'lose')
            elif guessed_number > correct_answer:
                print(correct_answer)
                flash("Your guess was too High! Try Guessing a Lower Number", 'high')
                remaining_points -= 1
                return render_template('guessing.html', point=remaining_points)
            elif guessed_number < correct_answer:
                flash("Your guess was too Low! Try guessing a higher number.", 'low')
                print(correct_answer)
                remaining_points -= 1
                return render_template('guessing.html', point=remaining_points)
            else:
                flash(f"Congratulations! You've Guessed it right! The secret Number is: {correct_answer}. Your Mind is Blowing Bro 🎉🎉", 'right')
                print(correct_answer)
                remaining_points = 6
                correct_answer = random.randint(1, 100)
                print(correct_answer)
                return redirect('/guessinggame')
        except Exception as e:
            flash(f"An error occurred: {str(e)}")
            return redirect('/guessinggame')
    return render_template('guessing.html', point=remaining_points)


@app.route('/contactus', methods=['GET', 'POST'])
def ContactUs():
    if request.method == 'POST':
        try:
            user_first_name = request.form['user_first_name']
            user_last_name = request.form['user_last_name']
            user_email = request.form['user_email']
            user_message = request.form['user_message']
            subject = "RajaTubeGrab Contact Us Form"
            sender = user_email
            recipients = ['ry360596@gmail.com']
            body = f"First Name: {user_first_name}\nLast Name: {user_last_name}\nEmail: {user_email}\n\nMessage:\n{user_message}"
            msg = Message(subject=subject, sender=sender, recipients=recipients)
            msg.body = body
            mail.send(msg)
            flash("Thanks for reaching out! We've received your message and will get back to you shortly.", 'success_email')
            return redirect('/contactus')
        except Exception as e:
            flash(f"An error occurred: {str(e)}", 'error_email')
            return redirect('/contactus')
    return render_template('contactus.html')

@app.route('/downloading_video=144p')
def Video144p():
    global user_url
    try:
        yt = YouTube(user_url)
        video = yt.streams.filter(res='144p').first()
        if video:
            video.download()
            flash("Video Downloaded Successfully!", 'success')
        else:
            flash("144P Stream are Not! Available, Please Select another Stream!", 'error')
    except Exception as e:
        flash(f"An error occurred: {str(e)}", 'error')

    return render_template('index.html')


@app.route('/downloading_video=240p')
def Video240p():
    global user_url
    try:
        yt = YouTube(user_url)
        video = yt.streams.filter(res='240p').first()
        if video:
            video.download()
            flash("Video Downloaded Successfully!", 'success')
        else:
            flash("240p Stream are Not! Available, Please Select another Stream!", 'error')
    except Exception as e:
        flash(f"An error occurred: {str(e)}", 'error')

    return render_template('index.html')


@app.route('/downloading_video=360p')
def Video360p():
    global user_url
    try:
        yt = YouTube(user_url)
        video = yt.streams.filter(res='360p').first()
        if video:
            video.download()
            flash("Video Downloaded Successfully!", 'success')
        else:
            flash("360p Stream are Not! Available, Please Select another Stream!", 'error')
    except Exception as e:
        flash(f"An error occurred: {str(e)}", 'error')

    return render_template('index.html')


@app.route('/downloading_video=480p')
def Video480p():
    global user_url
    try:
        yt = YouTube(user_url)
        video = yt.streams.filter(res='480p').first()
        if video:
            video.download()
            flash("Video Downloaded Successfully!", 'success')
        else:
            flash("480p Stream are Not! Available, Please Select another Stream!", 'error')
    except Exception as e:
        flash(f"An error occurred: {str(e)}", 'error')

    return render_template('index.html')


@app.route('/downloading_video=720p')
def Video720p():
    global user_url
    try:
        yt = YouTube(user_url)
        video = yt.streams.filter(res='720p').first()
        if video:
            video.download()
            flash("Video Downloaded Successfully!", 'success')
        else:
            flash("720p Stream are Not! Available, Please Select another Stream!", 'error')
    except Exception as e:
        flash(f"An error occurred: {str(e)}", 'error')

    return render_template('index.html')


@app.route('/downloading_video=1080p')
def Video1080p():
    global user_url
    try:
        yt = YouTube(user_url)
        video = yt.streams.filter(res='1080p').first()
        if video:
            video.download()
            flash("Video Downloaded Successfully!", 'success')
        else:
            flash("1080p (HD) Stream are Not! Available, Please Select another Stream!", 'error')
    except Exception as e:
        flash(f"An error occurred: {str(e)}", 'error')

    return render_template('index.html')


@app.route('/downloading_video=2k')
def Video2k():
    global user_url
    try:
        yt = YouTube(user_url)
        video = yt.streams.filter(res='1440p').first()
        if video:
            video.download()
            flash("Video Downloaded Successfully!", 'success')
        else:
            flash("1440p (2K) Stream are Not! Available, Please Select another Stream!", 'error')
    except Exception as e:
        flash(f"An error occurred: {str(e)}", 'error')

    return render_template('index.html')


@app.route('/downloading_video=4k')
def Video4k():
    global user_url
    try:
        yt = YouTube(user_url)
        video = yt.streams.filter(res='2160p').first()
        if video:
            video.download()
            flash("Video Downloaded Successfully!", 'success')
        else:
            flash("2160p(4K) Stream are Not! Available, Please Select another Stream!", 'error')
    except Exception as e:
        flash(f"An error occurred: {str(e)}", 'error')

    return render_template('index.html')


@app.route('/downloading_audio')
def Audio():
    global user_url
    try:
        yt = YouTube(user_url)
        audio = yt.streams.filter(only_audio=True).first()
        if audio:
            audio.download()
            flash("Audio Downloaded Successfully!", 'success')
        else:
            flash("Error Downloading Audio!", 'error')
    except Exception as e:
        flash(f"An error occurred: {str(e)}", 'error')

    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
