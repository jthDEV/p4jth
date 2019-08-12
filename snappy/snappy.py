import boto3
import click

session = boto3.Session(profile_name="snappy")
ec2 = session.resource('ec2')

@click.group()
def cli():
	"""Manage Snappy"""

@cli.group('volumes')
def volumes():
	"""Commands to manage volumes"""


@cli.group('instances')
def instances():
		"""Commands to manage instances"""

@instances.command('list')
@click.option('--project', default=None, help="Only instances of with tag <tag> will be handled")

def list_instances(project):
	"""list EC2 instances"""
	instances = []

	if project:
		print('Filtering by tag '+project)
		filters = [{'Name':'tag:Project', 'Values':[project]}]
		instances = ec2.instances.filter(Filters=filters)
		print(str(len(list(instances)))+' instance(s) found:')
	else: 
 		print('No filter set, taking all...')
 		instances = ec2.instances.all()

	for i in instances :
	    print(', '.join((
	    i.id,
	    i.instance_type,
	    i.placement['AvailabilityZone'],
	    i.state['Name'],
	    i.public_dns_name)))

	return

@instances.command('stop')
@click.option('--project', default=None, help="Only instances of with tag <tag> will be handled")

def stop_instances(project):
	"""Stop EC2 instances"""
	instances = []

	if project:
		print('Filtering by tag '+project)
		filters = [{'Name':'tag:Project', 'Values':[project]}]
		instances = ec2.instances.filter(Filters=filters)
		print(str(len(list(instances)))+' instance(s) found:')
	else: 
 		print('No filter set, taking all...')
 		instances = ec2.instances.all()

	for i in instances :
		print('Stopping instance {0}'.format(i.id))
		i.stop()


@instances.command('start')
@click.option('--project', default=None, help="Only instances of with tag <tag> will be handled")

def start_instances(project):
	"""Start EC2 instances"""
	
	instances = []

	if project:
		print('Filtering by tag '+project)
		filters = [{'Name':'tag:Project', 'Values':[project]}]
		instances = ec2.instances.filter(Filters=filters)
		print(str(len(list(instances)))+' instance(s) found:')
	else: 
 		print('No filter set, taking all...')
 		instances = ec2.instances.all()

	for i in instances :
		print('Starting instance {0}'.format(i.id))
		i.start()


if __name__ == '__main__' :

	cli()
	



	

