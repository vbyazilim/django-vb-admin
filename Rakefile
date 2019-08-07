task :clean do
  rm_rf "build"
  rm_rf "dist"
  rm_rf "django_vb_admin.egg-info"
  puts "Build files are removed..."
end

desc "Build package"
task :build => [:clean] do
  system "python setup.py sdist bdist_wheel"
end

desc "Upload package"
task :upload => [:build] do
  system "twine upload dist/*"
end

AVAILABLE_REVISIONS = ["major", "minor", "patch"]
desc "Bump version"
task :bump, [:revision] do |t, args|
  args.with_defaults(revision: "patch")
  abort "Please provide valid revision: #{AVAILABLE_REVISIONS.join(',')}" unless AVAILABLE_REVISIONS.include?(args.revision)
  system "bumpversion #{args.revision}"
end
