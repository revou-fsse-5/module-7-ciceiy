from flask import Blueprint, render_template, request
from services.user_service import role_required

reviewBp = Blueprint('review', __name__)

@reviewBp.route('/review', methods=['GET', 'POST'])
@role_required('admin')
def submit_review():
    if request.method == 'POST':
        pass
    return render_template('review.html')