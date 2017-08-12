from django.db import models
from django.core.urlresolvers import reverse
from organizer.models import Startup, Tag


class Post(models.Model):
    title = models.CharField(max_length=63)
    slug = models.SlugField(max_length=63,
                            help_text='A label for URL config',
                            unique_for_month='pub_date'
                            )
    text = models.TextField()
    pub_date = models.DateField('date published',
                                auto_now_add=True
                                )
    tags = models.ManyToManyField(Tag, related_name='blog_posts')
    startups = models.ManyToManyField(Startup, related_name='blog_posts')

    def __str__(self):
        return "{} on {}".format(
            self.title,
            self.pub_date.strftime('%Y-%m-%d')
        )

    def get_absolute_url(self):
        # note this is a django standard method- vs function w/ similar purpose below
        return reverse(
            'blog_post_detail',
            kwargs={'year': self.pub_date.year,
                    'month': self.pub_date.month,
                    'slug': self.slug
                    }
        )

    def get_update_url(self):
        # this is a book creation for similar function as above but for updates
        # not a standard method that django will look for - see chap 9, pg 258
        return reverse(
            'blog_post_update',
            kwargs={'year': self.pub_date.year,
                    'month': self.pub_date.month,
                    'slug': self.slug
                    }
        )

    def get_delete_url(self):
        return reverse(
            'blog_post_delete',
            kwargs={'year': self.pub_date.year,
                    'month': self.pub_date.month,
                    'slug': self.slug
                    }
        )

    class Meta:
        verbose_name = 'blog post'
        ordering = ['-pub_date', 'title']
        get_latest_by = 'pub_date'





