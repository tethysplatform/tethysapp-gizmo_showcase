from django.shortcuts import render, redirect
from django.urls import reverse
from tethys_sdk.permissions import login_required
from tethys_sdk.gizmos import JobsTable
from .common import docs_endpoint


@login_required()
def jobs_table(request):
    """
    Controller for the Jobs Table page.
    """
    from tethys_compute.models import TethysJob
    jobs = TethysJob.objects.filter(label='gizmos_showcase').order_by('id').select_subclasses()

    # Table View
    jobs_table_options = JobsTable(
        jobs=jobs,
        column_fields=('id', 'name', 'description', 'creation_time'),
        hover=True,
        striped=False,
        bordered=False,
        condensed=False,
        monitor_url='gizmo_showcase:jobs_table_results',
        results_url='gizmo_showcase:jobs_table_results',
        refresh_interval=10000,
        run_btn=True,
        delete_btn=True,
        show_detailed_status=True,
        actions=['run', 'resubmit', 'log', 'monitor', 'results', 'terminate', 'delete'],
    )

    context = {
        'docs_endpoint': docs_endpoint,
        'jobs_table': jobs_table_options
    }
    return render(request, 'gizmo_showcase/jobs_table.html', context)


def jobs_table_results(request, job_id):
    """Controller for the Jobs Table demo results links."""
    return redirect(reverse('gizmo_showcase:jobs_table'))


def create_sample_jobs(request):
    """Controller that creates sample Jobs for the Jobs Table demo."""
    from tethys_compute.models import BasicJob, CondorWorkflow
    def create_job(job_id, description, status, status_msg=None, workflow=False):
        Job = CondorWorkflow if workflow else BasicJob
        job = Job(
            name=f'job_{job_id}',
            user=request.user,
            description=description,
            label='gizmos_showcase',
            status_message=status_msg,
            _status=status,
        )
        job.save()

    for i, (desc, status) in enumerate((
            ('Pending job', 'PEN'),
            ('Submitted job', 'SUB'),
            ('Running job', 'RUN'),
            ('Job error', 'ERR'),
            ('Aborted job', 'ABT'),
            ('Completed job', 'COM'),
    )):
        create_job(i, desc, status)
        create_job(i + 10, desc, status, status_msg=f'{desc} status message')

    create_job('20', 'Running multi-process job with various statuses', 'VAR')
    create_job('21', 'Completed multi-process job with some errors', 'VCP')
    create_job('22', 'Workflow job with multiple nodes.', 'VAR', workflow=True)

    return redirect(reverse('gizmo_showcase:jobs_table'))
