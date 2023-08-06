"""Custom forms."""

from django import forms
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

from modoboa.lib import form_utils
from modoboa.parameters import forms as param_forms


class ReportOptionsForm(forms.Form):
    """Report display options."""

    current_year = forms.IntegerField(widget=forms.widgets.HiddenInput)
    current_week = forms.IntegerField()
    query = forms.ChoiceField(
        choices=[("previous", "Previous"), ("next", "Next")])
    resolve_hostnames = forms.BooleanField(
        initial=False, required=False)

    def __init__(self, *args, **kwargs):
        """Constructor."""
        super(ReportOptionsForm, self).__init__(*args, **kwargs)
        if not args:
            year, week, day = timezone.now().isocalendar()
            self.fields["current_year"].initial = year
            self.fields["current_week"].initial = week


class ParametersForm(param_forms.AdminParametersForm):
    """Extension settings."""

    app = "modoboa_dmarc"

    qsettings_sep = form_utils.SeparatorField(label=_("DNS settings"))

    enable_rlookups = form_utils.YesNoField(
        label=_("Enable reverse lookups"),
        initial=False,
        help_text=_(
            "Enable reverse DNS lookups (reports will be longer to display)"
        )
    )
