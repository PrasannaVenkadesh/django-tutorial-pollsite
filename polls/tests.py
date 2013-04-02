"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

import datetime

from django.core.urlresolvers import reverse
from django.test import TestCase
from django.utils import timezone

from polls.models import Poll

class PollMethodTest(TestCase):
	def test_was_recently_published_with_future_poll(self):
			future_poll = Poll(pub_date=timezone.now() + datetime.timedelta(days=1))
			self.assertEqual(future_poll.was_recently_published(), False)

	def test_was_recently_published_with_old_poll(self):
			old_poll = Poll(pub_date=timezone.now() - datetime.timedelta(days=30))
			self.assertEqual(old_poll.was_recently_published(), False)

	def test_was_recently_published_with_recent_poll(self):
			recent_poll = Poll(pub_date=timezone.now() + datetime.timedelta(hours=1))
			self.assertEqual(recent_poll.was_recently_published(), False)	


def create_poll(question, days):
	return Poll.objects.create(
			question=question,
			pub_date = timezone.now() + datetime.timedelta(days=days)
		)

class PollViewTest(TestCase):
	def test_index_view_with_no_polls(self):
		#If no poll(s) exists appropriate message should be returned
		response = self.client.get(reverse('polls:index'))
		self.assertEqual(response.status_code,200)
		self.assertContains(response,"No Polls are available.")
		self.assertQuerysetEqual(response.context['latest_list'],[])

	def test_index_view_with_a_past_poll(self):
		#checks if the test returns a poll added with a past date
		create_poll(question='Past Poll.', days=-30)
		response = self.client.get(reverse('polls:index'))
		self.assertQuerysetEqual(response.context['latest_list'],['<Poll: Past Poll.>'])

	def test_index_view_with_a_future_poll(self):
		#test should not returns a poll added with a future date
		create_poll(question='Future poll.', days=30)
		response = self.client.get(reverse('polls:index'))
		self.assertContains(response, 'No Polls are available', status_code=200)
		self.assertQuerysetEqual(response.context['latest_list'],[])

	def test_index_view_with_future_poll_and_past_poll(self):
		create_poll(question='Past Poll.',days=-30)
		create_poll(question='Future Poll.',days=30)
		response = self.client.get(reverse('polls:index'))
		self.assertQuerysetEqual(response.context['latest_list'],['<Poll: Past Poll.>'])

	def test_index_view_with_two_past_polls(self):
		create_poll(question='Past Poll 1.',days=-30)
		create_poll(question='Past Poll 2.',days=-5)
		response=self.client.get(reverse('polls:index'))
		self.assertQuerysetEqual(response.context['latest_list'],['<Poll: Past Poll 1.>', '<Poll: Past Poll 2.>'])


