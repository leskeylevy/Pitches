from . import main
from flask import render_template, url_for, redirect
from flask_login import login_required, current_user
from .forms import PitchForm, CommentForm
from ..models import Pitch


@main.route('/', methods=['GET', 'POST'])
def index():
    form = PitchForm()
    if form.validate_on_submit():
        title = form.title.data
        content = form.content.data

        new_pitch = Pitch(title=title, content=content)
        new_pitch.save_pitch()

        return redirect(url_for('.index'))

    pitch = Pitch.get_pitch_order()

    return render_template('index.html', PitchForm=form, pitch=pitch)


@main.route('/user/<uname>/update', methods=['GET', 'POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username=uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile', uname=user.username))

    return render_template('profile/update.html', form=form)


@main.route('/personal', methods=['GET', 'POST'])
@login_required
def new_pitch(category):
    form = PitchForm()
    if form.validate_on_submit():
        category = form.category.data
        title = form.title.data
        content = form.content.data

        # UPdated pitch instance
        new_pitch = Pitch(category=pitch.category, title=pitch.title, content=pitch.content, user=current_user)

        # save pitch method
        new_pitch.save_pitch()
        return render_template(url_for('.pitch', category=pitch.category))

    title = f'{pitch.category} pitch'
    return render_template('new_pitch.html', title=title, pitch_form=form, pitch=pitch)


@main.route('/comment/<int:id>', methods=['GET', 'POST'])
@login_required
def comment(id):
    comment_form = CommentForm()
    # pitch = Pitch.query.get(id)
    if comment_form.validate_on_submit():
        comment_form = comment_form.comment.data

        # updating comments
        new_comment = Comment(comment=comment, user=current_user, id=id)
        # saving comments
        new_comment.save_comment()
        return redirect(url_for('main.index'))
    return render_template('comment.html', comment_form=comment_form, pitch=pitch)
